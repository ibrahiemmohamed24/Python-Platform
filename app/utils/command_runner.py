import subprocess


class CommandRunner:
    @staticmethod
    def run(
        command: list[str],
        *,
        allowed_return_codes: set[int] | None = None,
        timeout_seconds: float = 30.0,
    ) -> subprocess.CompletedProcess[str]:
        """
        Execute an external command and return the result.
        """
        expected_codes = (
            allowed_return_codes
            if allowed_return_codes is not None
            else {0}
        )

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                stdin=subprocess.DEVNULL,
                timeout=timeout_seconds,
            )
        except FileNotFoundError as exc:
            raise RuntimeError(
                f"Command not found: {command[0]}"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(
                f"Command timed out after {timeout_seconds:g} seconds: "
                f"{command[0]}"
            ) from exc

        if result.returncode not in expected_codes:
            details = (result.stderr or result.stdout).strip()
            if len(details) > 500:
                details = f"{details[:497]}..."

            message = (
                f"Command failed with exit code {result.returncode}: "
                f"{command[0]}"
            )
            if details:
                message = f"{message}: {details}"

            raise RuntimeError(message)

        return result

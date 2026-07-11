import subprocess


class CommandRunner:
    @staticmethod
    def run(command: list[str]) -> subprocess.CompletedProcess:
        """
        Execute an external command and return the result.
        """
        try:
            return subprocess.run(
                command,
                capture_output=True,
                text=True,
            )
        except FileNotFoundError as exc:
            raise RuntimeError(
                f"Command not found: {command[0]}"
            ) from exc
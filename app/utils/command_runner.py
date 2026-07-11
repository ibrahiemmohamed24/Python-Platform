import subprocess


class CommandRunner:
    @staticmethod
    def run(command: list[str]) -> subprocess.CompletedProcess:
        """
        Execute an external command and return the result.
        """
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
        )
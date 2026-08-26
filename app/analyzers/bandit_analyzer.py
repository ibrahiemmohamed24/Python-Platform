import json
import sys

from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult
from app.parsers.bandit_parser import BanditParser
from app.utils.command_runner import CommandRunner


class BanditAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            [
                sys.executable,
                "-m",
                "bandit",
                "-f",
                "json",
                "--",
                file_path,
            ],
            allowed_return_codes={0, 1},
        )

        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Bandit returned invalid JSON output") from exc

        if not isinstance(data, dict):
            raise RuntimeError("Bandit returned an unexpected JSON payload")

        errors = data.get("errors")
        if errors:
            first_error = errors[0]
            reason = (
                first_error.get("reason", "unknown error")
                if isinstance(first_error, dict)
                else str(first_error)
            )
            raise RuntimeError(f"Bandit failed: {reason}")

        results = data.get("results")
        if not isinstance(results, list):
            raise RuntimeError("Bandit response is missing a results list")

        issues = BanditParser.parse(results)

        return AnalysisResult(
            analyzer="Bandit",
            success=len(issues) == 0,
            issues=issues,
        )

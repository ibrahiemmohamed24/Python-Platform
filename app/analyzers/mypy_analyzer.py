import json
import sys

from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult
from app.parsers.mypy_parser import MypyParser
from app.utils.command_runner import CommandRunner


class MypyAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            [
                sys.executable,
                "-m",
                "mypy",
                "--output",
                "json",
                "--",
                file_path,
            ],
            allowed_return_codes={0, 1},
        )

        if result.returncode == 1 and not result.stdout.strip():
            details = result.stderr.strip() or "no error details"
            raise RuntimeError(f"Mypy failed: {details}")

        try:
            issues = MypyParser.parse(result.stdout)
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            raise RuntimeError("Mypy returned invalid JSON output") from exc

        return AnalysisResult(
            analyzer="Mypy",
            success=len(issues) == 0,
            issues=issues,
        )

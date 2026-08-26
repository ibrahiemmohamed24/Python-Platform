import json
import sys

from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult
from app.parsers.ruff_parser import RuffParser
from app.utils.command_runner import CommandRunner


class RuffAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            [
                sys.executable,
                "-m",
                "ruff",
                "check",
                "--output-format",
                "json",
                "--",
                file_path,
            ],
            allowed_return_codes={0, 1},
        )

        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Ruff returned invalid JSON output") from exc

        if not isinstance(data, list):
            raise RuntimeError("Ruff returned an unexpected JSON payload")

        issues = RuffParser.parse(data)

        return AnalysisResult(
            analyzer="Ruff",
            success=len(issues) == 0,
            issues=issues,
        )

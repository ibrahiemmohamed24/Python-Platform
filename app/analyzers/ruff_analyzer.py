import json

from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult
from app.parsers.ruff_parser import RuffParser
from app.utils.command_runner import CommandRunner


class RuffAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            [
                "ruff",
                "check",
                file_path,
                "--output-format",
                "json",
            ]
        )

        issues = RuffParser.parse(
            json.loads(result.stdout)
        )

        return AnalysisResult(
            analyzer="Ruff",
            success=len(issues) == 0,
            issues=issues,
        )
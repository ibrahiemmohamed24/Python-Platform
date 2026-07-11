import json

from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult
from app.parsers.bandit_parser import BanditParser
from app.utils.command_runner import CommandRunner


class BanditAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            [
                "bandit",
                "-f",
                "json",
                file_path,
            ]
        )

        data = json.loads(result.stdout)

        issues = BanditParser.parse(
            data["results"]
        )

        return AnalysisResult(
            analyzer="Bandit",
            success=len(issues) == 0,
            issues=issues,
        )
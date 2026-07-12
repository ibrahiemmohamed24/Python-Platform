from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult
from app.parsers.mypy_parser import MypyParser
from app.utils.command_runner import CommandRunner


class MypyAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            [
                "mypy",
                "--output",
                "json",
                file_path,
            ]
        )

        

        issues = MypyParser.parse(result.stdout)

        return AnalysisResult(
            analyzer="Mypy",
            success=len(issues) == 0,
            issues=issues,
        )
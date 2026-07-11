from app.analyzers.base_analyzer import BaseAnalyzer
from app.contracts.analysis_result import AnalysisResult
from app.utils.command_runner import CommandRunner


class RuffAnalyzer(BaseAnalyzer):
    def analyze(self, file_path: str) -> AnalysisResult:
        result = CommandRunner.run(
            ["ruff", "check", file_path]
        )

        return AnalysisResult(
            analyzer="Ruff",
            success=result.returncode == 0,
            issues=[],
        )
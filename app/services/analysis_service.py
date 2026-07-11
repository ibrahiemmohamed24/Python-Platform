from app.analyzers.bandit_analyzer import BanditAnalyzer
from app.analyzers.analyzer_manager import AnalyzerManager
from app.analyzers.ruff_analyzer import RuffAnalyzer
from app.domain.analysis_result import AnalysisResult


class AnalysisService:
    def __init__(self) -> None:
        self.manager = AnalyzerManager()

        self.manager.register(RuffAnalyzer())
        self.manager.register(BanditAnalyzer())

    def analyze(self, file_path: str) -> list[AnalysisResult]:
        return self.manager.analyze(file_path)
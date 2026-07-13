from app.registry.analyzer_registry import AnalyzerRegistry
from app.domain.analysis_result import AnalysisResult


class AnalysisService:
    def __init__(self) -> None:
        self.manager = AnalyzerRegistry.build()

  

    def analyze(self, file_path: str) -> list[AnalysisResult]:
        return self.manager.analyze(file_path)
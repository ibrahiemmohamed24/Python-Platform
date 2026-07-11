from app.analyzers.base_analyzer import BaseAnalyzer
from app.domain.analysis_result import AnalysisResult


class AnalyzerManager:
    def __init__(self) -> None:
        self._analyzers: list[BaseAnalyzer] = []

    def register(self, analyzer: BaseAnalyzer) -> None:
        self._analyzers.append(analyzer)

    def analyze(self, file_path: str) -> list[AnalysisResult]:
        results: list[AnalysisResult] = []

        for analyzer in self._analyzers:
            results.append(analyzer.analyze(file_path))

        return results
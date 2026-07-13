from app.analyzers.base_analyzer import BaseAnalyzer

class AnalyzerFactory:

    @staticmethod
    def create(analyzer: type[BaseAnalyzer]) -> BaseAnalyzer:
        return analyzer()
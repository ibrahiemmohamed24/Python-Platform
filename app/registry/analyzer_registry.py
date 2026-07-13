from app.analyzers.analyzer_manager import AnalyzerManager
from app.factory.analyzer_factory import AnalyzerFactory
from app.analyzers.ruff_analyzer import RuffAnalyzer
from app.analyzers.bandit_analyzer import BanditAnalyzer
from app.analyzers.mypy_analyzer import MypyAnalyzer


class AnalyzerRegistry:

    @staticmethod
    def build() -> AnalyzerManager:
        manager = AnalyzerManager()
        manager.register(AnalyzerFactory.create(RuffAnalyzer))
        manager.register(AnalyzerFactory.create(BanditAnalyzer))
        manager.register(AnalyzerFactory.create(MypyAnalyzer))

        return manager
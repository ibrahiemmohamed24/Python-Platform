from app.analyzers.analyzer_manager import AnalyzerManager

from app.analyzers.ruff_analyzer import RuffAnalyzer
from app.analyzers.bandit_analyzer import BanditAnalyzer
from app.analyzers.mypy_analyzer import MypyAnalyzer


class AnalyzerRegistry:

    @staticmethod
    def build() -> AnalyzerManager:
        manager = AnalyzerManager()
        manager.register(RuffAnalyzer())
        manager.register(BanditAnalyzer())
        manager.register(MypyAnalyzer())

        return manager
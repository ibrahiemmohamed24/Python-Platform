from app.analyzers.ruff_analyzer import RuffAnalyzer
from app.domain.analysis_result import AnalysisResult


def test_ruff_analyzer():
    analyzer = RuffAnalyzer()

    result = analyzer.analyze("sample.py")

    assert isinstance(result, AnalysisResult)

    assert result.analyzer == "Ruff"
    assert result.success is False
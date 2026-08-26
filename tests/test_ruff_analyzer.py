from pathlib import Path

from app.analyzers.ruff_analyzer import RuffAnalyzer
from app.domain.analysis_result import AnalysisResult


SAMPLE_FILE = Path(__file__).resolve().parents[1] / "sample.py"


def test_ruff_analyzer():
    analyzer = RuffAnalyzer()

    result = analyzer.analyze(str(SAMPLE_FILE))

    assert isinstance(result, AnalysisResult)

    assert result.analyzer == "Ruff"
    assert result.success is False

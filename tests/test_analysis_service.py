from app.services.analysis_service import AnalysisService


def test_analysis_service():
    service = AnalysisService()

    results = service.analyze("sample.py")

    assert len(results) == 1

    result = results[0]

    assert result.analyzer == "Ruff"
    assert result.success is False
    assert len(result.issues) == 2

    assert result.issues[0].code == "F401"
    assert result.issues[1].code == "F841"
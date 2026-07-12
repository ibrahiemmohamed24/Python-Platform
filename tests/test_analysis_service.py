from app.services.analysis_service import AnalysisService


def test_analysis_service():
    service = AnalysisService()

    results = service.analyze("sample.py")

    assert len(results) == 3

    ruff_result = next(
        result for result in results
        if result.analyzer == "Ruff"
    )

    bandit_result = next(
        result for result in results
        if result.analyzer == "Bandit"
    )

    mypy_result = next(
        result for result in results
        if result.analyzer == "Mypy"
    )

    assert ruff_result.success is False
    assert len(ruff_result.issues) == 2

    assert ruff_result.issues[0].code == "F401"
    assert ruff_result.issues[1].code == "F841"

    assert bandit_result.success is True
    assert bandit_result.issues == []

    assert mypy_result.success is True
    assert mypy_result.issues == []
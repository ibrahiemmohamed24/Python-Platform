from pathlib import Path

import pytest
from pydantic import ValidationError

from app.schemas.analyze_request import AnalyzeRequest


def test_accepts_existing_python_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sample_file = tmp_path / "sample.py"
    sample_file.write_text("print('hello')\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    request = AnalyzeRequest(file_path="sample.py")

    assert request.file_path == str(sample_file.resolve())


@pytest.mark.parametrize("file_path", ["", "--fix"])
def test_rejects_empty_or_option_like_paths(file_path: str) -> None:
    with pytest.raises(ValidationError):
        AnalyzeRequest(file_path=file_path)


def test_rejects_file_outside_analysis_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    analysis_root = tmp_path / "workspace"
    analysis_root.mkdir()
    outside_file = tmp_path / "outside.py"
    outside_file.write_text("print('outside')\n", encoding="utf-8")
    monkeypatch.chdir(analysis_root)

    with pytest.raises(ValidationError):
        AnalyzeRequest(file_path=str(outside_file))

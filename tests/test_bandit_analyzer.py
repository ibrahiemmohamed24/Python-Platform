import json
import subprocess

import pytest

from app.analyzers.bandit_analyzer import BanditAnalyzer
from app.utils.command_runner import CommandRunner


def test_reports_bandit_execution_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    completed_process = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout=json.dumps(
            {
                "errors": [{"reason": "No such file or directory"}],
                "results": [],
            }
        ),
        stderr="",
    )

    def fake_run(
        command: list[str],
        **kwargs: object,
    ) -> subprocess.CompletedProcess[str]:
        return completed_process

    monkeypatch.setattr(CommandRunner, "run", fake_run)

    with pytest.raises(RuntimeError, match="No such file or directory"):
        BanditAnalyzer().analyze("missing.py")

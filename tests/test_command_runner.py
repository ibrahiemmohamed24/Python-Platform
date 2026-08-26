import sys

import pytest

from app.utils.command_runner import CommandRunner


def test_allows_expected_nonzero_return_code() -> None:
    result = CommandRunner.run(
        [sys.executable, "-c", "raise SystemExit(1)"],
        allowed_return_codes={0, 1},
    )

    assert result.returncode == 1


def test_rejects_unexpected_return_code() -> None:
    with pytest.raises(RuntimeError, match="exit code 2"):
        CommandRunner.run(
            [sys.executable, "-c", "raise SystemExit(2)"],
        )


def test_times_out() -> None:
    with pytest.raises(RuntimeError, match="timed out"):
        CommandRunner.run(
            [sys.executable, "-c", "import time; time.sleep(1)"],
            timeout_seconds=0.01,
        )

# Contributing

Thank you for helping build AI Python QA Platform. The project is intentionally
developed in small steps so each architectural change remains understandable
and reversible.

## Before you start

1. Discuss large features or architectural changes in an issue first.
2. Keep each pull request focused on one concern.
3. Do not replace or complete placeholder layers unless the related design has
   been agreed.
4. Never commit credentials, local environments, caches, or generated reports.

## Development setup

Create and activate a Python 3.13+ virtual environment, then run:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Required checks

Run these checks before submitting a pull request:

```bash
python -m ruff check app tests
python -m mypy app tests
python -m pytest
python -m build
```

## Pull requests

- Explain the problem and the chosen solution.
- Add or update tests for behavior changes.
- Mention any known limitations or follow-up work.
- Keep formatting-only changes separate from functional changes.
- Use clear, single-purpose commit messages.

By contributing, you confirm that you have the right to submit your work under
the license that the project adopts. A license must be selected before the
project is presented as open source.

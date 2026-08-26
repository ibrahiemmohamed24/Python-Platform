# AI Python QA Platform

An early-stage Python quality-assurance API that runs Ruff, Bandit, and Mypy
against a Python file and returns one normalized response.

> **Project status:** active foundation work. The API is suitable for local
> development and evaluation, but it is not ready to expose directly to the
> public internet. The provider layer is intentionally being built in small,
> verified steps.

## What works today

- FastAPI application with root, health, and analysis endpoints.
- Ruff, Bandit, and Mypy analyzer integrations.
- A shared domain model and API response mapper.
- Analyzer registration through a registry and factory.
- Validation that limits analysis to an existing Python file, no larger than
  1 MB, inside the directory where the API process was started.

## Requirements

- Python 3.13 or newer.
- Git for contributing.

## Local setup

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Install the project and development tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the API

Start the server from the directory that contains the files you want the API
to analyze:

```bash
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

Example request, when `sample.py` is inside the server's working directory:

```bash
curl -X POST http://127.0.0.1:8000/analysis/ \
  -H "Content-Type: application/json" \
  -d '{"file_path":"sample.py"}'
```

The current API accepts a path on the server, not a file from the caller's
computer. A future public deployment should replace this contract with an
isolated upload or source-code job model.

## Verify changes

```bash
python -m ruff check app tests
python -m mypy app tests
python -m pytest
python -m build
```

## Architecture

The current request flow is:

```text
FastAPI router
  -> analysis service
  -> analyzer registry / factory
  -> analyzer manager
  -> Ruff, Bandit, and Mypy analyzers
  -> parsers and domain models
  -> response mapper
```

The empty or minimal layers are deliberate extension points, not finished
features. Keep architectural changes small and independently verified.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Security
reports should follow [SECURITY.md](SECURITY.md).

## License

No open-source license has been selected yet. Until a license file is added,
the repository is publicly visible source code but is not legally ready for
open-source reuse or distribution.

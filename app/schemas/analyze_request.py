from pathlib import Path

from pydantic import BaseModel
from pydantic import field_validator


MAX_ANALYSIS_FILE_SIZE_BYTES = 1_000_000


class AnalyzeRequest(BaseModel):
    file_path: str

    @field_validator("file_path")
    @classmethod
    def validate_file_path(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value or cleaned_value.startswith("-"):
            raise ValueError("file_path must be a Python file path")

        analysis_root = Path.cwd().resolve()

        try:
            resolved_path = Path(cleaned_value).resolve(strict=True)
        except (OSError, RuntimeError) as exc:
            raise ValueError("file_path must point to an existing file") from exc

        try:
            resolved_path.relative_to(analysis_root)
        except ValueError as exc:
            raise ValueError(
                "file_path must be inside the analysis root"
            ) from exc

        if not resolved_path.is_file() or resolved_path.suffix.lower() != ".py":
            raise ValueError("file_path must point to a Python file")

        try:
            file_size = resolved_path.stat().st_size
        except OSError as exc:
            raise ValueError("file_path could not be inspected") from exc

        if file_size > MAX_ANALYSIS_FILE_SIZE_BYTES:
            raise ValueError("file_path must be 1 MB or smaller")

        return str(resolved_path)

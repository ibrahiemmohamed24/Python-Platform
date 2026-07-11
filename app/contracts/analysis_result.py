from dataclasses import dataclass, field

from app.contracts.issue import Issue


@dataclass
class AnalysisResult:
    analyzer: str
    success: bool
    issues: list[Issue] = field(default_factory=list)
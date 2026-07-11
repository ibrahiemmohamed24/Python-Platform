from dataclasses import dataclass


@dataclass
class Issue:
    code: str
    message: str
    severity: str
    line: int
    column: int
    source: str
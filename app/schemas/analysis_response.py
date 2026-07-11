from pydantic import BaseModel


class IssueResponse(BaseModel):
    code: str
    message: str
    severity: str
    line: int
    column: int
    source: str


class AnalyzerResponse(BaseModel):
    analyzer: str
    success: bool
    issues: list[IssueResponse]


class AnalysisResponse(BaseModel):
    success: bool
    results: list[AnalyzerResponse]
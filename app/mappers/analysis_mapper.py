from app.contracts.analysis_result import AnalysisResult
from app.contracts.issue import Issue
from app.schemas.analysis_response import (
    AnalysisResponse,
    AnalyzerResponse,
    IssueResponse,
)


class AnalysisMapper:
    @staticmethod
    def to_issue_response(issue: Issue) -> IssueResponse:
        return IssueResponse(
            code=issue.code,
            message=issue.message,
            severity=issue.severity,
            line=issue.line,
            column=issue.column,
            source=issue.source,
        )

    @staticmethod
    def to_analyzer_response(result: AnalysisResult) -> AnalyzerResponse:
        return AnalyzerResponse(
            analyzer=result.analyzer,
            success=result.success,
            issues=[
                AnalysisMapper.to_issue_response(issue)
                for issue in result.issues
            ],
        )

    @staticmethod
    def to_response(results: list[AnalysisResult]) -> AnalysisResponse:
        return AnalysisResponse(
            success=all(result.success for result in results),
            results=[
                AnalysisMapper.to_analyzer_response(result)
                for result in results
            ],
        )
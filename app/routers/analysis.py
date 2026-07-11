from fastapi import APIRouter

from app.mappers.analysis_mapper import AnalysisMapper
from app.schemas.analyze_request import AnalyzeRequest
from app.schemas.analysis_response import AnalysisResponse
from app.services.analysis_service import AnalysisService

router = APIRouter(prefix="/analysis", tags=["Analysis"])

service = AnalysisService()


@router.post("/", response_model=AnalysisResponse)
def analyze(request: AnalyzeRequest):
    results = service.analyze(request.file_path)
    return AnalysisMapper.to_response(results)
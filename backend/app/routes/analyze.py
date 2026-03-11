from fastapi import APIRouter
from app.models.request_models import AnalyzeLiftRequest
from app.models.response_models import AnalyzeLiftResponse, LiftIssue
from app.services.analysis_service import analyze_lift_data

router = APIRouter(prefix="/analyze-lift", tags=["analyze"])

@router.post("", response_model=AnalyzeLiftResponse)
async def analyze_lift(request: AnalyzeLiftRequest):

    result = analyze_lift_data(request)
    issues = [LiftIssue(**issue) for issue in result["issues"]]

    return AnalyzeLiftResponse(
        exercise_type=request.exercise_type,
        rep_count=result["rep_count"],
        score=result["score"],
        feedback=result["feedback"],
        issues=issues
    )
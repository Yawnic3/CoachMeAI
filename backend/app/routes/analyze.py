from fastapi import APIRouter
from app.models.request_models import AnalyzeLiftRequest
from app.models.response_models import AnalyzeLiftResponse, LiftIssue
from app.services.scoring import score_lift
from app.services.feedback import generate_feedback

router = APIRouter(prefix="/analyze-lift", tags=["analyze"])

@router.post("", response_model=AnalyzeLiftResponse)
async def analyze_lift(request: AnalyzeLiftRequest):

    result = score_lift(request)

    feedback = generate_feedback(
        exercise_type=request.exercise_type,
        score=result["score"],
        issues=result["issues"]
    )

    issues = [LiftIssue(**issue) for issue in result["issues"]]

    return AnalyzeLiftResponse(
        exercise_type=request.exercise_type,
        rep_count=result["rep_count"],
        score=result["score"],
        feedback=feedback,
        issues=issues
    )
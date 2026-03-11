from fastapi import APIRouter
from app.models.request_models import AnalyzeLiftRequest
from app.models.response_models import AnalyzeLiftResponse, LiftIssue

router = APIRouter(prefix="/analyze-lift", tags=["analyze"])

@router.post("", response_model=AnalyzeLiftResponse)
async def analyze_lift(request: AnalyzeLiftRequest):

    mock_issues = [
        LiftIssue(issue="Knees caving in", severity="medium", message="Your knees are collapsing inward during the squat. Focus on pushing them out."),
        LiftIssue(issue="Back rounding", severity="high", message="Your back is rounding at the bottom of the squat. Try to keep it straight and engage your core.")
    ]
    return AnalyzeLiftResponse(
        exercise_type=request.exercise_type,
        rep_count=10,
        score=85,
        feedback="Good form overall, but try to keep your back straighter.",
        issues=mock_issues
    )
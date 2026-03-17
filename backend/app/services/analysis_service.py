from app.models.request_models import AnalyzeLiftRequest
from app.services.scoring import score_lift
from app.services.feedback import generate_feedback

def analyze_lift_data(request: AnalyzeLiftRequest) -> dict:
    scoring_result = score_lift(request)

    feedback = generate_feedback(
        exercise_type=request.exercise_type,
        score=scoring_result["score"],
        issues=scoring_result["issues"]
    )

    return {
        "exercise_type": request.exercise_type,
        "rep_count": scoring_result["rep_count"],
        "score": scoring_result["score"],
        "feedback": feedback,
        "issues": scoring_result["issues"]
    }
from app.models.request_models import AnalyzeLiftRequest


def score_lift(request: AnalyzeLiftRequest) -> dict:
    exercise = request.exercise_type.lower()

    if exercise == "squat":
        return {
            "rep_count": 6,
            "score": 78,
            "issues": [
                {
                    "issue": "knee_valgus",
                    "severity": "medium",
                    "message": "Your knees move inward slightly during the descent."
                },
                {
                    "issue": "torso_lean",
                    "severity": "low",
                    "message": "Your torso leans forward slightly near the bottom of the rep."
                }
            ]
        }

    if exercise == "deadlift":
        return {
            "rep_count": 5,
            "score": 74,
            "issues": [
                {
                    "issue": "back_rounding",
                    "severity": "medium",
                    "message": "Your upper back rounds slightly during the pull."
                },
                {
                    "issue": "hip_rise",
                    "severity": "low",
                    "message": "Your hips rise a little too early off the floor."
                }
            ]
        }

    if exercise == "bench":
        return {
            "rep_count": 8,
            "score": 81,
            "issues": [
                {
                    "issue": "elbow_flare",
                    "severity": "medium",
                    "message": "Your elbows flare outward during the press."
                }
            ]
        }

    return {
        "rep_count": 0,
        "score": 60,
        "issues": [
            {
                "issue": "unknown_exercise",
                "severity": "low",
                "message": "Exercise type not fully supported yet."
            }
        ]
    }
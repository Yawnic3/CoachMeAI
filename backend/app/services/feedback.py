def generate_feedback(exercise_type: str, score: int, issues: list[dict]) -> str:
    if not issues:
        return f"Great job on your {exercise_type}. Your form looked solid overall."

    messages = [issue["message"] for issue in issues]

    if score >= 85:
        intro = f"Strong {exercise_type} overall."
    elif score >= 70:
        intro = f"Good effort on your {exercise_type}."
    else:
        intro = f"Your {exercise_type} needs some improvement."

    return intro + " Focus on the following: " + " ".join(messages)
from pydantic import BaseModel
from typing import List

class LiftIssue(BaseModel):
    issue: str
    severity: str
    message: str

class AnalyzeLiftResponse(BaseModel):
    exercise_type: str
    rep_count: int
    score: int
    feedback: str
    issues: List[LiftIssue]
from pydantic import BaseModel, Field
from typing import Optional

class AnalyzeLiftRequest(BaseModel):
    exercise_type: str = Field(..., example="squat")
    video_url: Optional[str] = Field(None, example="https://example.com/video.mp4") 
    user_id: Optional[str] = Field(None, example="user_123") 
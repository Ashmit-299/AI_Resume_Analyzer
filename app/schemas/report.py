from pydantic import BaseModel
from typing import List


class ReportResponse(BaseModel):

    overall_score: float

    semantic_score: float

    required_skill_score: float

    ats_score: float

    matched_skills: List[str]

    missing_skills: List[str]

    feedback: str

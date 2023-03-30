from typing import Optional
from pydantic import BaseModel

class _LanguagePair(BaseModel):
    sourceLanguage: str
    targetLanguage: Optional[str]

class FeedbackSubmitRequest(BaseModel):
    language: _LanguagePair
    example: str
    rating: int
    comments: str
    service_id: str
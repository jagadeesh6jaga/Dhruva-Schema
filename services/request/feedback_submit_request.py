from pydantic import BaseModel

class FeedbackSubmitRequest(BaseModel):
    language: str
    example: str
    rating: int
    comments: str
    service_id: str
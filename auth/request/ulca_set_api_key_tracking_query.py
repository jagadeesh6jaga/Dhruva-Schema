from pydantic import BaseModel, EmailStr


class ULCASetApiKeyTrackingQuery(BaseModel):
    emailId: EmailStr
    appName: str
    dataTracking: bool

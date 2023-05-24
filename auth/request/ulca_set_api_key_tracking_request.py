from pydantic import BaseModel, EmailStr


class ULCASetApiKeyTrackingRequest(BaseModel):
    emailId: EmailStr
    appName: str
    dataTracking: bool

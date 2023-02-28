from pydantic import BaseModel, EmailStr


class SignInResponse(BaseModel):
    email: EmailStr
    token: str
    role: str

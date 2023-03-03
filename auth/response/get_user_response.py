from pydantic import BaseModel, EmailStr


class GetUserResponse(BaseModel):
    name: str
    email: EmailStr
    role: str

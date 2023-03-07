from pydantic import BaseModel, EmailStr

from ..common.role_type import RoleType


class SignInResponse(BaseModel):
    email: EmailStr
    token: str
    role: RoleType

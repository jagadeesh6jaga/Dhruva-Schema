from pydantic import BaseModel


class ApiKey(BaseModel):
    name: str
    masked_key: str
    active: bool
    type: str

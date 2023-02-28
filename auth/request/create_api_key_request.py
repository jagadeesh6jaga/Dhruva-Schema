from enum import Enum

from pydantic import BaseModel


class ApiKeyType(Enum):
    PLATFORM = "PLATFORM"
    INFERENCE = "INFERENCE"


class CreateApiKeyRequest(BaseModel):
    name: str
    type: ApiKeyType

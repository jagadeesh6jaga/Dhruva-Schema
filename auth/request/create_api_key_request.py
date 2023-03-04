import re
from enum import Enum

from pydantic import BaseModel, validator


class ApiKeyType(Enum):
    PLATFORM = "PLATFORM"
    INFERENCE = "INFERENCE"


class CreateApiKeyRequest(BaseModel):
    name: str
    type: ApiKeyType = ApiKeyType.INFERENCE

    @validator("name")
    def check_api_key_name_format(cls, v):
        name_regex = r"^[a-z0-9\.\-@_\/]+$"
        if not re.search(name_regex, v):
            raise ValueError("Name has invalid characters")
        return v

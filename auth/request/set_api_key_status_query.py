from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ApiKeyAction(Enum):
    ACTIVATE = "ACTIVATE"
    REVOKE = "REVOKE"


class SetApiKeyStatusQuery(BaseModel):
    api_key_name: str
    target_user_id: Optional[str]
    action: ApiKeyAction

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ApiKeyTrackingAction(Enum):
    ENABLE = "ENABLE"
    DISABLE = "REVOKE"
    
class SetApiKeyTrackingQuery(BaseModel):
    api_key_name: str
    target_user_id: Optional[str]
    action: ApiKeyTrackingAction

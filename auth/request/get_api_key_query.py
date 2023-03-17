from typing import Optional
from pydantic import BaseModel


class GetApiKeyQuery(BaseModel):
    api_key_name: str
    target_user_id: Optional[str]

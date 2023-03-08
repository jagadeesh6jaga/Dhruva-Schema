from typing import Optional

from pydantic import BaseModel


class GetAllApiKeysRequest(BaseModel):
    target_user_id: Optional[str] = None

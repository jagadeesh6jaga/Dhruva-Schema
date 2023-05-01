from typing import Any, Dict, Optional

from pydantic import BaseModel, root_validator


class ModifyApiKeyParamsQuery(BaseModel):
    api_key_name: str
    target_user_id: Optional[str]
    active: Optional[bool]
    data_tracking: Optional[bool]

    @root_validator()
    def check_and_fetch_audio(cls, values: Dict[str, Any]):
        if values.get("active") == None and values.get("data_tracking") == None:
            raise ValueError("Atleast one of data_tracking or active must be provided")
        else:
            return values

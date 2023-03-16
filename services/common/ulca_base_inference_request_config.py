from pydantic import BaseModel
from typing import Optional

class _ULCABaseInferenceRequestConfig(BaseModel):
    serviceId: Optional[str] = ""

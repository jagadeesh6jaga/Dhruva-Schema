from typing import Optional
from pydantic import BaseModel

class ULCAGenericInferenceRequestWithoutConfig(BaseModel):
    input: Optional[list[dict]]
    audio: Optional[list[dict]]

class ULCAGenericInferenceRequest(ULCAGenericInferenceRequestWithoutConfig):
    config: dict

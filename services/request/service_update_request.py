from pydantic import BaseModel
from typing import Optional
from ..common import _ULCALanguagePair

class ServiceUpdateRequest(BaseModel):
    serviceId: str
    name: Optional[str]
    serviceDescription: Optional[str]
    languagePair: Optional[_ULCALanguagePair]
    hardwareDescription: Optional[str]
    endpoint: Optional[str]
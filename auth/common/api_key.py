from typing import Optional, List
from pydantic import BaseModel


class _ServiceUsage(BaseModel):
    service_id: str
    usage: int


class ApiKey(BaseModel):
    name: str
    masked_key: str
    active: bool
    type: str
    services: List[_ServiceUsage]

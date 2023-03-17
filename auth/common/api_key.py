from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class _ServiceUsage(BaseModel):
    service_id: str
    usage: int


class ApiKey(BaseModel):
    name: str
    masked_key: str
    active: bool
    type: str
    created_timestamp: datetime
    services: List[_ServiceUsage]

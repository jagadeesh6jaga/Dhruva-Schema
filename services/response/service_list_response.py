from ..common import _ULCATask
from typing import List
from .service_response import ServiceResponse

class ServiceListResponse(ServiceResponse):
    task: _ULCATask
    languages: List[dict]

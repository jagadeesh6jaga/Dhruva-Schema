from typing import List
from ..common.dhruva_model import Model
from .service_response import ServiceResponse
from ...auth.response.get_all_api_keys_response import _ApiKey

class ServiceViewResponse(ServiceResponse):
    model: Model
    key_usage: List[_ApiKey] = []
    total_usage: int = 0

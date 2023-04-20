from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ..common import _ControlConfig, _ULCAAudio


class ULCAGenericInferenceRequestWithoutConfig(BaseModel):
    input: Optional[List[Dict[str, Any]]]
    audio: List[_ULCAAudio]


class ULCAGenericInferenceRequest(ULCAGenericInferenceRequestWithoutConfig):
    config: dict
    controlConfig: _ControlConfig

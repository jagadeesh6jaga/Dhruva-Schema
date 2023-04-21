from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ..common import _ControlConfig, _ULCAAudio, _ULCAText


class ULCAGenericInferenceRequestWithoutConfig(BaseModel):
    input: Optional[List[_ULCAText]]
    audio: Optional[List[_ULCAAudio]]


class ULCAGenericInferenceRequest(ULCAGenericInferenceRequestWithoutConfig):
    config: dict
    controlConfig: _ControlConfig

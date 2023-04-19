from typing import Optional

from pydantic import BaseModel

from ..common import _ControlConfig


class ULCAGenericInferenceRequestWithoutConfig(BaseModel):
    input: Optional[list[dict]]
    audio: Optional[list[dict]]


class ULCAGenericInferenceRequest(ULCAGenericInferenceRequestWithoutConfig):
    config: dict
    controlConfig: _ControlConfig

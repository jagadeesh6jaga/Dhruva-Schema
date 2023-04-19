from pydantic import BaseModel, create_model

from ..common import (
    _ControlConfig,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
    _ULCATtsInferenceConfig,
)

_ULCATtsInferenceRequestConfig = create_model(
    "_ULCATtsInferenceRequestConfig",
    __base__=(_ULCATtsInferenceConfig, _ULCABaseInferenceRequestConfig),
)


class ULCATtsInferenceRequest(BaseModel):
    input: list[_ULCAText]
    config: _ULCATtsInferenceRequestConfig
    controlConfig: _ControlConfig

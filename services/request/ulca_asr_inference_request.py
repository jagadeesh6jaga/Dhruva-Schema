from pydantic import BaseModel, create_model

from ..common import (
    _ControlConfig,
    _ULCAAudio,
    _ULCABaseAudioConfig,
    _ULCABaseInferenceRequestConfig,
)

_ULCAAsrInferenceRequestConfig = create_model(
    "_ULCAAsrInferenceRequestConfig",
    __base__=(_ULCABaseAudioConfig, _ULCABaseInferenceRequestConfig),
)


class ULCAAsrInferenceRequest(BaseModel):
    audio: list[_ULCAAudio]
    config: _ULCAAsrInferenceRequestConfig
    controlConfig: _ControlConfig

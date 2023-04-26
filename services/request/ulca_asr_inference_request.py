from typing import List

from pydantic import create_model

from ..common import (
    _ULCAAudio,
    _ULCABaseAudioConfig,
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
)

_ULCAAsrInferenceRequestConfig = create_model(
    "_ULCAAsrInferenceRequestConfig",
    __base__=(_ULCABaseAudioConfig, _ULCABaseInferenceRequestConfig),
)


class ULCAAsrInferenceRequest(_ULCABaseInferenceRequest):
    audio: List[_ULCAAudio]
    config: _ULCAAsrInferenceRequestConfig

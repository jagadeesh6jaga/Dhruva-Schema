from pydantic import create_model

from ..common import (
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
    _ULCATtsInferenceConfig,
)

_ULCATtsInferenceRequestConfig = create_model(
    "_ULCATtsInferenceRequestConfig",
    __base__=(_ULCATtsInferenceConfig, _ULCABaseInferenceRequestConfig),
)


class ULCATtsInferenceRequest(_ULCABaseInferenceRequest):
    input: list[_ULCAText]
    config: _ULCATtsInferenceRequestConfig

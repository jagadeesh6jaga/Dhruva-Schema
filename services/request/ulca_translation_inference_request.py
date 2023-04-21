from pydantic import create_model

from ..common import (
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
    _ULCATranslationInferenceConfig,
)

_ULCATranslationInferenceRequestConfig = create_model(
    "_ULCATranslationInferenceRequestConfig",
    __base__=(_ULCATranslationInferenceConfig, _ULCABaseInferenceRequestConfig),
)


class ULCATranslationInferenceRequest(_ULCABaseInferenceRequest):
    input: list[_ULCAText]
    config: _ULCATranslationInferenceRequestConfig

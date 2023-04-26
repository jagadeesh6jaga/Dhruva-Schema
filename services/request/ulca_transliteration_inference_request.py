from pydantic import create_model

from ..common import (
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
    _ULCATransliterationInferenceConfig,
)

_ULCATransliterationInferenceRequestConfig = create_model(
    "_ULCATransliterationInferenceRequestConfig",
    __base__=(_ULCATransliterationInferenceConfig, _ULCABaseInferenceRequestConfig),
)


class ULCATransliterationInferenceRequest(_ULCABaseInferenceRequest):
    input: list[_ULCAText]
    config: _ULCATransliterationInferenceRequestConfig

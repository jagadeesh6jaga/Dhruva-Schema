from pydantic import BaseModel, create_model

from ..common import (
    _ControlConfig,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
    _ULCATranslationInferenceConfig,
)

_ULCATranslationInferenceRequestConfig = create_model(
    "_ULCATranslationInferenceRequestConfig",
    __base__=(_ULCATranslationInferenceConfig, _ULCABaseInferenceRequestConfig),
)


class ULCATranslationInferenceRequest(BaseModel):
    input: list[_ULCAText]
    config: _ULCATranslationInferenceRequestConfig
    controlConfig: _ControlConfig

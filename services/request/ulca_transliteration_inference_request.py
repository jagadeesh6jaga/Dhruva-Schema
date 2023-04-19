from pydantic import BaseModel, create_model

from ..common import (
    _ControlConfig,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
    _ULCATransliterationInferenceConfig,
)

_ULCATransliterationInferenceRequestConfig = create_model(
    "_ULCATransliterationInferenceRequestConfig",
    __base__=(_ULCATransliterationInferenceConfig, _ULCABaseInferenceRequestConfig),
)


class ULCATransliterationInferenceRequest(BaseModel):
    input: list[_ULCAText]
    config: _ULCATransliterationInferenceRequestConfig
    controlConfig: _ControlConfig

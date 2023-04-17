from pydantic import BaseModel, create_model
from ..common import _ULCAText, _ULCATransliterationInferenceConfig, _ULCABaseInferenceRequestConfig

_ULCATransliterationInferenceRequestConfig = create_model("_ULCATransliterationInferenceRequestConfig", __base__=(_ULCATransliterationInferenceConfig, _ULCABaseInferenceRequestConfig))

class ULCATransliterationInferenceRequest(BaseModel):
    input: list[_ULCAText]
    config: _ULCATransliterationInferenceRequestConfig

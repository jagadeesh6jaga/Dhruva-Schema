from pydantic import BaseModel, create_model
from ..common import _ULCAText, _ULCABaseMonolingualTaskConfig, _ULCABaseInferenceRequestConfig

_ULCANerInferenceRequestConfig = create_model("_ULCANerInferenceRequestConfig", __base__=(_ULCABaseMonolingualTaskConfig, _ULCABaseInferenceRequestConfig))

class ULCANerInferenceRequest(BaseModel):
    input: list[_ULCAText]
    config: _ULCANerInferenceRequestConfig

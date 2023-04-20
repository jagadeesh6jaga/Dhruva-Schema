from typing import List
from pydantic import BaseModel, create_model

from ..common import (
    _ControlConfig,
    _ULCABaseInferenceRequestConfig,
    _ULCABaseMonolingualTaskConfig,
    _ULCAText,
)

_ULCANerInferenceRequestConfig = create_model(
    "_ULCANerInferenceRequestConfig",
    __base__=(_ULCABaseMonolingualTaskConfig, _ULCABaseInferenceRequestConfig),
)


class ULCANerInferenceRequest(BaseModel):
    input: List[_ULCAText]
    config: _ULCANerInferenceRequestConfig
    controlConfig: _ControlConfig

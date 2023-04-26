from typing import List

from pydantic import create_model

from ..common import (
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
    _ULCABaseMonolingualTaskConfig,
    _ULCAText,
)

_ULCANerInferenceRequestConfig = create_model(
    "_ULCANerInferenceRequestConfig",
    __base__=(_ULCABaseMonolingualTaskConfig, _ULCABaseInferenceRequestConfig),
)


class ULCANerInferenceRequest(_ULCABaseInferenceRequest):
    input: List[_ULCAText]
    config: _ULCANerInferenceRequestConfig

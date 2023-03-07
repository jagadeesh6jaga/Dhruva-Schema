from typing import Optional
from pydantic import BaseModel
from ..common import _ULCATextPair, _ULCATranslationInferenceConfig, _ULCATaskType


class ULCATranslationInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.TRANSLATION
    output: list[_ULCATextPair]
    config: Optional[_ULCATranslationInferenceConfig]

from typing import Optional
from pydantic import BaseModel
from ..common import _ULCAText, _ULCABaseAudioConfig, _ULCATaskType


class ULCAAsrInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.ASR
    output: list[_ULCAText]
    config: Optional[_ULCABaseAudioConfig]

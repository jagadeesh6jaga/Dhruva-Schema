from typing import List, Optional

from pydantic import BaseModel

from ..common import _ULCABaseAudioConfig, _ULCATaskType, _ULCAText


class ULCAAsrInferenceResponseConfig(_ULCABaseAudioConfig):
    postProcessors: List[str]


class ULCAAsrInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.ASR
    output: List[_ULCAText]
    config: Optional[ULCAAsrInferenceResponseConfig] = None

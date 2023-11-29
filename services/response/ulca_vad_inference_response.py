from typing import Dict, List

from pydantic import BaseModel

from ..common import _ULCATaskType


class _ULCATimestamps(BaseModel):
    timestamps: List[Dict[str, float]]


class ULCAVadInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.VAD
    output: List[_ULCATimestamps]

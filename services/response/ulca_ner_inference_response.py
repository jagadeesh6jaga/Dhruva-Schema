from pydantic import BaseModel
from typing import List, Optional
from ..common import _ULCAText, _ULCATaskType

class _ULCANerTokenPrediction(BaseModel):
    token: Optional[str]
    tag: str
    tokenIndex: Optional[int]
    tokenStartIndex: int
    tokenEndIndex: int

class _ULCANerPrediction(_ULCAText):
    nerPrediction: List[_ULCANerTokenPrediction]

class ULCANerInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.NER
    output: List[_ULCANerPrediction]

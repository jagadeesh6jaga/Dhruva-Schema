from typing import Optional
from pydantic import BaseModel
from module.services.model.model import *
from module.services.model.model import _InferenceEndPoint,_Benchmark,_Submitter
from schema.services.common.ulca_task import _ULCATask
class ModelUpdateRequest(BaseModel):
    id: str
    name: Optional[str]
    description: Optional[str]
    refUrl: str
    task: _ULCATask
    languages: List[dict]
    license: str
    domain: List[str]
    inferenceEndPoint: _InferenceEndPoint
    benchmarks: Optional[List[_Benchmark]]
    submitter: _Submitter
    
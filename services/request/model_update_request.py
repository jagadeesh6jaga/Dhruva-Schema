from typing import Optional
from pydantic import BaseModel
from module.services.model.model import *
from module.services.model.model import _InferenceEndPoint,_Benchmark,_Submitter
from schema.services.common.ulca_task import _ULCATask
class ModelUpdateRequest(BaseModel):
    modelId: str
    name: Optional[str]
    description: Optional[str]
    refUrl: Optional[str]
    task: Optional[_ULCATask]
    languages: Optional[List[dict]]
    license: Optional[str]
    domain: Optional[List[str]]
    inferenceEndPoint: Optional[_InferenceEndPoint]
    benchmarks: Optional[List[_Benchmark]]
    submitter: Optional[_Submitter]
    
from pydantic import BaseModel
from typing import Optional
from .ulca_generic_inference_request import ULCAGenericInferenceRequestWithoutConfig
from ..common import _ULCABaseMonolingualTaskConfig, _ULCATask

class _ULCAPipelineTask(BaseModel):
    serviceId: Optional[str]
    task: _ULCATask
    config: dict

class ULCAPipelineInferenceRequest(BaseModel):
    taskSequence: list[_ULCAPipelineTask]
    entryData: ULCAGenericInferenceRequestWithoutConfig

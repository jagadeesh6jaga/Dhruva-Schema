from pydantic import BaseModel
from .ulca_generic_inference_request import ULCAGenericInferenceRequestWithoutConfig
from ..common import _ULCABaseMonolingualTaskConfig, _ULCATask

class _ULCAPipelineTask(BaseModel):
    serviceId: str
    task: _ULCATask
    config: dict

class ULCAPipelineInferenceRequest(BaseModel):
    taskSequence: list[_ULCAPipelineTask]
    entryData: ULCAGenericInferenceRequestWithoutConfig

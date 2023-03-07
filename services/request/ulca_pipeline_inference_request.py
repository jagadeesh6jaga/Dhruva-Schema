from pydantic import BaseModel
from typing import Optional
from .ulca_generic_inference_request import ULCAGenericInferenceRequestWithoutConfig
from ..common import _ULCABaseMonolingualTaskConfig, _ULCATaskType

class _ULCAPipelineTask(BaseModel):
    serviceId: Optional[str]
    taskType: _ULCATaskType
    config: dict

class ULCAPipelineInferenceRequest(BaseModel):
    pipelineTasks: list[_ULCAPipelineTask]
    inputData: ULCAGenericInferenceRequestWithoutConfig

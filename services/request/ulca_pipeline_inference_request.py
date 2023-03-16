from pydantic import BaseModel
from typing import Optional, Union
from .ulca_generic_inference_request import ULCAGenericInferenceRequestWithoutConfig
from ..common import _ULCABaseMonolingualTaskConfig, _ULCATaskType
from .ulca_translation_inference_request import _ULCATranslationInferenceRequestConfig
from .ulca_asr_inference_request import _ULCAAsrInferenceRequestConfig
from .ulca_tts_inference_request import _ULCATtsInferenceRequestConfig

class _ULCAPipelineTask(BaseModel):
    taskType: _ULCATaskType
    config: dict
    # config: Union[_ULCATranslationInferenceRequestConfig, _ULCAAsrInferenceRequestConfig, _ULCATtsInferenceRequestConfig]

class ULCAPipelineInferenceRequest(BaseModel):
    pipelineTasks: list[_ULCAPipelineTask]
    inputData: ULCAGenericInferenceRequestWithoutConfig

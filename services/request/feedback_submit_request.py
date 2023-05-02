from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel

from ..response import ULCAGenericInferenceResponse
from ..common import (
    _ULCATaskType,
    _ControlConfig,
)
from . import (
    _ULCATranslationInferenceRequestConfig,
    _ULCATransliterationInferenceRequestConfig,
    _ULCATtsInferenceRequestConfig,
    _ULCAAsrInferenceRequestConfig,
    _ULCANerInferenceRequestConfig
)
from .ulca_generic_inference_request import ULCAGenericInferenceRequestWithoutConfig


class _FeedbackType(str, Enum):
    RATING = "rating"
    COMMENT = "comment"
    THUMBS = "thumbs"
    RATING_LIST = "ratingList"
    COMMENT_LIST = "commentList"
    THUMBS_LIST = "thumbsList"
    CHECKBOX_LIST = "checkboxList"


class _LanguagePair(BaseModel):
    sourceLanguage: str
    targetLanguage: Optional[str]


class RequestConfig(BaseModel):
    taskType: _ULCATaskType
    config: Union[
        _ULCANerInferenceRequestConfig,
        _ULCATranslationInferenceRequestConfig,
        _ULCATransliterationInferenceRequestConfig,
        _ULCAAsrInferenceRequestConfig,
        _ULCATtsInferenceRequestConfig,
    ]

class PipelineOutput(BaseModel):
    controlConfig: _ControlConfig
    pipelineResponse: List[ULCAGenericInferenceResponse]


class PipelineInput(BaseModel):
    pipelineTasks: List[RequestConfig]
    inputData: List[ULCAGenericInferenceRequestWithoutConfig]
    controlConfig: _ControlConfig


class BaseFeedbackType(BaseModel):
    parameterName: str


class FeedbackTypeRating(BaseFeedbackType):
    rating: int


class FeedbackTypeCheckbox(BaseFeedbackType):
    isSelected: bool


class FeedbackTypeComment(BaseFeedbackType):
    comment: str


class FeedbackTypeThumbs(BaseFeedbackType):
    isLiked: bool


class CommonFeedback(BaseModel):
    question: str
    feedbackType: _FeedbackType
    comment: Optional[str]
    isLiked: Optional[bool]
    rating: Optional[int]


class GranularFeedback(CommonFeedback):
    checkboxList: Optional[List[FeedbackTypeCheckbox]]
    ratingList: Optional[List[FeedbackTypeRating]]
    commentList: Optional[List[FeedbackTypeComment]]
    thumbsList: Optional[List[FeedbackTypeThumbs]]


class TaskFeedback(BaseModel):
    taskType: _ULCATaskType
    commonFeedback: List[CommonFeedback]
    granularFeedback: Optional[List[GranularFeedback]]


class PipelineFeedback(BaseModel):
    commonFeedback: List[CommonFeedback]


class ULCAFeedbackRequest(BaseModel):
    feedbackTimeStamp: Optional[int]
    feedbackLanguage: str
    pipelineInput: PipelineInput
    pipelineOutput: Optional[PipelineOutput]
    suggestedPipelineOutput: Optional[PipelineOutput]
    pipelineFeedback: Optional[PipelineFeedback]
    taskFeedback: Optional[List[TaskFeedback]]

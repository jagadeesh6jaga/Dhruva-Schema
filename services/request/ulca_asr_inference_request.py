from enum import Enum
from typing import List, Optional

from ..common import (
    _ULCAAudio,
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
)
from ..common.ulca_base_audio_config import _ULCABaseAudioConfig


class ULCATextFormat(str, Enum):
    SRT = "srt"
    TRANSCRIPT = "transcript"
    WEBVTT = "webvtt"


class _ULCAAsrInferenceRequestConfig(
    _ULCABaseInferenceRequestConfig, _ULCABaseAudioConfig
):
    postProcessors: Optional[list[str]]
    transcriptionFormat: ULCATextFormat = ULCATextFormat.TRANSCRIPT


class ULCAAsrInferenceRequest(_ULCABaseInferenceRequest):
    audio: List[_ULCAAudio]
    config: _ULCAAsrInferenceRequestConfig

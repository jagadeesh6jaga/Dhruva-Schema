from typing import List, Optional

from pydantic import create_model

from ..common import (
    _ULCAAudio,
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
)
from ..common.ulca_base_audio_config import _ULCABaseAudioConfig


class _ULCAAsrInferenceRequestConfig(
    _ULCABaseInferenceRequestConfig, _ULCABaseAudioConfig
):
    postProcessors: Optional[list[str]]


class ULCAAsrInferenceRequest(_ULCABaseInferenceRequest):
    audio: List[_ULCAAudio]
    config: _ULCAAsrInferenceRequestConfig

from typing import Literal

from pydantic import BaseModel

from ..common import _ControlConfig, _ULCABaseAudioConfig, _ULCALanguagePair
from .ulca_asr_inference_request import ULCAAsrInferenceRequest


class _ULCAS2SInferenceConfig(_ULCABaseAudioConfig):
    language: _ULCALanguagePair
    gender: Literal["male", "female"]


class ULCAS2SInferenceRequest(ULCAAsrInferenceRequest):
    config: _ULCAS2SInferenceConfig
    controlConfig: _ControlConfig

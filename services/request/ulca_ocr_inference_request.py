from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from ..common import (
    _ULCAIamge,
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
)
from ..common.ulca_base_image_config import _ULCABaseImageConfig


class _ULCAOcrInferenceRequestConfig(
    _ULCABaseInferenceRequestConfig, _ULCABaseImageConfig
):
    pass


class ULCAOcrnferenceRequest(_ULCABaseInferenceRequest):
    image: List[_ULCAIamge]
    config: _ULCAOcrInferenceRequestConfig

from pydantic import BaseModel
from typing import Optional

from .ulca_control_config import _ControlConfig


class _ULCABaseInferenceRequest(BaseModel):
    controlConfig: Optional[_ControlConfig]

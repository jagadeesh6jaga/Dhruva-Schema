from pydantic import BaseModel

from .ulca_control_config import _ControlConfig


class _ULCABaseInferenceRequest(BaseModel):
    controlConfig: _ControlConfig

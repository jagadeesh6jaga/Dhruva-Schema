from typing import Any, Dict, List, Optional

from ..common import _ULCAAudio, _ULCABaseInferenceRequest, _ULCAText


class ULCAGenericInferenceRequestWithoutConfig(_ULCABaseInferenceRequest):
    input: Optional[List[_ULCAText]]
    audio: Optional[List[_ULCAAudio]]


class ULCAGenericInferenceRequest(ULCAGenericInferenceRequestWithoutConfig):
    config: dict

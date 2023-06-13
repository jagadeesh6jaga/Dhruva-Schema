from ..common import (
    _ULCABaseInferenceRequest,
    _ULCAText,
    _ULCATranslationInferenceConfig,
)
from ..common.ulca_language_pair import _ULCALanguagePair


class ULCATranslationInferenceRequest(_ULCABaseInferenceRequest):
    input: list[_ULCAText]
    config: _ULCATranslationInferenceConfig

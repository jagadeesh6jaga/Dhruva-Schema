from pydantic import BaseModel
from .ulca_language_pair import _ULCALanguagePair


class _ULCATransliterationInferenceConfig(BaseModel):
    language: _ULCALanguagePair
    isSentence: bool = True
    numSuggestions: int = 5

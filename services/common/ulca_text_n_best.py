from typing import Dict, List, Optional

from pydantic import BaseModel

from .ulca_text import _ULCAText


class _NBestToken(BaseModel):
    word: str
    tokens: List[Dict[str, float]]

class _ULCATextNBest(_ULCAText):
    nBestTokens: Optional[List[_NBestToken]] = None

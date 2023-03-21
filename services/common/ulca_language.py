from pydantic import BaseModel
from typing import Optional

class _ULCALanguage(BaseModel):
    sourceLanguage: str
    sourceScriptCode: Optional[str] = ""

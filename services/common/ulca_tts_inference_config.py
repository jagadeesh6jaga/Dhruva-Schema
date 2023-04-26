from typing import Literal, Optional
from .ulca_base_monolingual_config import _ULCABaseMonolingualTaskConfig


class _ULCATtsInferenceConfig(_ULCABaseMonolingualTaskConfig):
    gender: Literal["male", "female"]
    samplingRate: Optional[int]
    audioFormat: Optional[Literal["wav", "mp3", "flac", "pcm", "flv","ogg"]]
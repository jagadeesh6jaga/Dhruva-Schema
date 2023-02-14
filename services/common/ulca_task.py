from pydantic import BaseModel

TRANSLATION_TASK_TYPE = "translation"
ASR_TASK_TYPE = "asr"
TTS_TASK_TYPE = "tts"
NER_TASK_TYPE = "ner"

class _ULCATask(BaseModel):
    type: str

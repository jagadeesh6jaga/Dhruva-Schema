from typing import List

from pydantic import BaseModel


class _ApiKey(BaseModel):
    # TODO: Add this field back once _id is correctly loaded in ApiKey model
    # id: str
    name: str
    masked_key: str
    active: bool
    type: str


class GetAllApiKeysResponse(BaseModel):
    api_keys: List[_ApiKey]

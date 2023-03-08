from pydantic import BaseModel


class GetApiKeyQuery(BaseModel):
    api_key_id: str

from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from ...common import ObjectIdField


class ServiceStatus(BaseModel):
    status: str
    lastUpdated: str
class ServiceResponse(BaseModel):
    id: ObjectIdField = Field(alias="_id")
    serviceId: str
    name: str
    serviceDescription: str
    hardwareDescription: str
    publishedOn: int
    modelId: str
    healthStatus: Optional[ServiceStatus]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
        }

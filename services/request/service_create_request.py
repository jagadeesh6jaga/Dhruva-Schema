from module.services.model import Service


class ServiceCreateRequest(Service):
    class Config:
        fields = {'id': {'exclude': True}}
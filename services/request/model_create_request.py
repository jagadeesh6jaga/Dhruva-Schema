from module.services.model import Model


class ModelCreateRequest(Model):
    class Config:
        fields = {'id': {'exclude': True}}
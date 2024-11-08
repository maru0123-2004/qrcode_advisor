from tortoise import Model
from tortoise.fields import UUIDField, CharField, ManyToManyRelation


class Stop(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=1024)
    odpt_id=CharField(max_length=512)
    lines:ManyToManyRelation["Line"]
    
from .line import Line
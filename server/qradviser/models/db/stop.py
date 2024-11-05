from tortoise import Model
from tortoise.fields import UUIDField, CharField, ManyToManyRelation


class Stop(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=1024)
    lines:ManyToManyRelation["Line"]
    
from .line import Line
from tortoise import Model
from tortoise.fields import UUIDField, CharField, ManyToManyRelation

from .array_fields import StrArrayField

class Stop(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=1024)
    odpt_ids=StrArrayField(default=[])
    lines:ManyToManyRelation["Line"]
    
from .line import Line
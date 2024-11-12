from tortoise import Model
from tortoise.fields import UUIDField, CharField, ManyToManyField, ManyToManyRelation

class Line(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=1024)
    company = CharField(max_length=1024)
    odpt_id=CharField(max_length=512)
    stops:ManyToManyRelation["Stop"] = ManyToManyField("models.Stop", related_name="lines", through="linestop")

from .stop import Stop
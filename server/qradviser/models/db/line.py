from tortoise import Model
from tortoise.fields import UUIDField, CharField, ManyToManyField

class Line(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=1024)
    company = CharField(max_length=1024)
    stops = ManyToManyField("models.Stop", related_name="lines")
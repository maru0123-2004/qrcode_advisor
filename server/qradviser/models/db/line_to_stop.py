from tortoise import Model
from tortoise.fields import ForeignKeyField, IntField

class LineStop(Model):
    stop = ForeignKeyField("models.Stop", related_name="stops")
    line = ForeignKeyField("models.Line", related_name="lines")
    order = IntField()
    class Meta:
        table = 'linestop'
        

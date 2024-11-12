from tortoise import Model
from tortoise.fields import ForeignKeyField, IntField

class LineStop(Model):
    stop_id = ForeignKeyField("models.Stop", related_name="stops")
    line_id = ForeignKeyField("models.Line", related_name="lines")
    order = IntField()
    class Meta:
        table = 'linestop'
        

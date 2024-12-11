from uuid import UUID
from pydantic import BaseModel
class StopData(BaseModel):
    stop_id: UUID
    name: str
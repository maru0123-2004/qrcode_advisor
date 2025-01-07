from typing import List, Union
from uuid import UUID
from pydantic import BaseModel
class StopData(BaseModel):
    stop_id: UUID
    name: str
    position: Union[List[float],None]
    distance: float=None
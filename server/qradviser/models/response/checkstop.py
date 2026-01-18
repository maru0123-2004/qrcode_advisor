from pydantic import BaseModel
from typing import List
from .search import StopData

class CheckStop(BaseModel):
    is_stopping: bool
    stops: List[StopData]=[]
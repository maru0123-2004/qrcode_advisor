from pydantic import BaseModel
class StopData(BaseModel):
    stop_id: int
    name: str
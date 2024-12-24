from pydantic import BaseModel


class Operator(BaseModel):
    id: str
    name: str
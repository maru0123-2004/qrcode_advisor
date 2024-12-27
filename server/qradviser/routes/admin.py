from typing import List
from fastapi.responses import StreamingResponse
from python_odpt import Client
from sse_starlette.sse import EventSourceResponse
from fastapi import APIRouter
from python_odpt.api.default import operator_operations_get_operators

from ..models.response.admin import Operator

from ..config import Settings

router=APIRouter(tags=["Admin"])
client=Client("http://api.odpt.org/api/v4/")

@router.get("/companies", response_model=List[Operator])
async def companies():
    operators=await operator_operations_get_operators.asyncio(client=client, aclconsumer_key=Settings().ODPT_TOKEN)
    return [
        Operator(id=com.owlsame_as, name=com.dctitle) for com in operators
    ]
        
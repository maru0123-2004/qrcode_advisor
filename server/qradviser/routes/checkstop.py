from typing import List
from uuid import UUID
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from ..exceptions import APIError
from .bus import get_bus
from passlib.context import CryptContext

from tortoise.expressions import Q

from ..models.db.stop import Stop
from ..models.db.line import Line
from ..models.db.line_to_stop import LineStop

router=APIRouter(tags=["CheckStop"])
crypt=CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/")
async def checkStop(dest_id: UUID, data: str):
    dest = await Stop.get(id=dest_id)
    bus = await get_bus(*data.split("."))
    line = await Line.get(odpt_id=bus.odptbusroute_pattern)
    start = await Stop.get(odpt_id=bus.odptstarting_busstop_pole)
    end = await Stop.get(odpt_id=bus.odptterminal_busstop_pole)
    start_ls = await LineStop.get(stop=start, line=line)
    dest_ls = await LineStop.get(stop=dest, line=line)
    end_ls = await LineStop.get(stop=end, line=line)
    if start_ls.order<=dest_ls.order and dest_ls.order<=end_ls.order:
        return True
    else:
        return False
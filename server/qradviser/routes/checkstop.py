from uuid import UUID
from fastapi import APIRouter
from typing import List, Union
from python_odpt import Client
from python_odpt.api.default import bus_operation_get_buses
from python_odpt.models import Bus

from ..exceptions import APIError, NotFound
from ..models.db.stop import Stop
from ..models.db.line_to_stop import LineStop
from ..config import Settings

router=APIRouter(tags=["CheckStop"])
client=Client("http://api.odpt.org/api/v4/")

async def get_bus(operator:str, number:int) -> Union[Bus, None]:
    buses:List[Bus]=await bus_operation_get_buses.asyncio(client=client, aclconsumer_key=Settings().ODPT_TOKEN, odptoperator=operator)
    try:
        for bus in buses:
            if bus.odptbus_number == number:
                return bus
        else:
            return None
    except:
        return None

@router.post("/", response_model=bool)
async def checkStop(dest_id: UUID, qrdata: str):
    dest = await Stop.get_or_none(id=dest_id)
    if dest is None:
        raise NotFound(detail="destination stop is not found")
    splited_data=qrdata.split(".")
    bus = await get_bus(".".join(splited_data[:-1]), splited_data[-1])
    if bus is None:
        raise NotFound(detail="no such bus found")
    start_ls = await LineStop.get_or_none(stop__odpt_ids__contains=bus.odptstarting_busstop_pole, line__odpt_id=bus.odptbusroute_pattern)
    end_ls = await LineStop.get_or_none(stop__odpt_ids__contains=bus.odptterminal_busstop_pole, line__odpt_id=bus.odptbusroute_pattern)
    prev_ls = await LineStop.get_or_none(stop__odpt_ids__contains=bus.odptfrom_busstop_pole, line__odpt_id=bus.odptbusroute_pattern)
    if start_ls is None or end_ls is None or prev_ls is None:
        raise APIError(status_code=500, detail="conflicted")
    dest_ls = await LineStop.get_or_none(stop=dest, line__odpt_id=bus.odptbusroute_pattern)
    if dest_ls is None:
        return False
    #From以降ならOK
    if prev_ls.order<=dest_ls.order and dest_ls.order<=end_ls.order:
        return True
    else:
        return False
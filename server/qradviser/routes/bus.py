from typing import List, Union
from python_odpt import Client
from python_odpt.api.default import bus_operation_get_buses
from python_odpt.models import Bus

from ..config import Settings

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
from os import environ
import argparse
from typing import List
from python_odpt import Client
from python_odpt.api.default import busroute_pattern_operations_get_busroute_patterns, busstop_pole_operations_get_busstop_poles
from python_odpt.models import BusroutePattern, BusstopPole

token=environ.get("ODPT_TOKEN", None)

parser=argparse.ArgumentParser()
parser.add_argument("company")
parser.add_argument("token", default=token)
args=parser.parse_args()
token=parser.token

client=Client("http://api.odpt.org/api/v4/")

from qradviser.db import DB_CONFIG
from qradviser.models.db import Line, Stop
from tortoise import Tortoise, run_async
async def main():
    await Tortoise.init(DB_CONFIG)
    stops=await busstop_pole_operations_get_busstop_poles.asyncio(client=client, aclconsumer_key=token, odptoperator=args.company)
    if not stops:
        return
    stops: List[BusstopPole]
    stops_db={}
    for stop in stops:
        st=await Stop.create(odpt_id=stop.owlsame_as,name=stop.dctitle)
        stops_db[st.odpt_id]=st
    lines=await busroute_pattern_operations_get_busroute_patterns.asyncio(client=client, aclconsumer_key=token, odptoperator=args.company)
    if not lines:
        return
    lines: List[BusroutePattern]
    for line in lines:
        l=await Line.create(name=line.dctitle, company=line.odptoperator, odpt_id=line.id) 
        for pole in line.odptbusstop_pole_order:
            if not pole.odptbusstop_pole in stops_db:
                print(pole.odptbusstop_pole)
                continue
            await l.stops.add(stops_db[pole.odptbusstop_pole])
run_async(main())

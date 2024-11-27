from os import environ
import argparse
from typing import List
from python_odpt import Client
from python_odpt.api.default import busroute_pattern_operations_get_busroute_patterns
from python_odpt.api.default import data_dump_operations_dump
from python_odpt.models import BusroutePattern, BusstopPole

token=environ.get("ODPT_TOKEN", None)

parser=argparse.ArgumentParser()
parser.add_argument("company")
parser.add_argument("-token", default=token, required=False)
args=parser.parse_args()
token=args.token

client=Client("http://api.odpt.org/api/v4/", follow_redirects=True)

from qradviser.db import DB_CONFIG
from qradviser.models.db import Line, Stop, LineStop
from tortoise import Tortoise, run_async
async def main():
    await Tortoise.init(DB_CONFIG)
    res=await data_dump_operations_dump.asyncio(client=client, aclconsumer_key=token, rdf_type="odpt:BusstopPole")
    if not res:
        return
    stops: List[BusstopPole]=res
    stops_db={}
    for stop in stops:
        if args.company not in stop.odptoperator:
            continue
        st,_=await Stop.get_or_create({"name":stop.dctitle,"pole_number":stop.odptbusstop_pole_number}, odpt_id=stop.owlsame_as)
        stops_db[st.odpt_id]=st
    lines=await data_dump_operations_dump.asyncio(client=client, aclconsumer_key=token, rdf_type="odpt:BusroutePattern")
    if not lines:
        return
    lines: List[BusroutePattern]
    for line in lines:
        if args.company != line.odptoperator:
            continue
        l,_=await Line.get_or_create({"name":line.dctitle, "company":line.odptoperator}, odpt_id=line.owlsame_as)
        for pole in line.odptbusstop_pole_order:
            if not pole.odptbusstop_pole in stops_db:
                print("Line not found:", pole.odptbusstop_pole)
                continue
            await LineStop.get_or_create({"order":pole.odptindex}, line=l, stop=stops_db[pole.odptbusstop_pole])
run_async(main())

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
from tortoise.exceptions import MultipleObjectsReturned
async def main():
    await Tortoise.init(DB_CONFIG)
    print("[1/5] Getting Stops... ", end="", flush=True)
    res=await data_dump_operations_dump.asyncio(client=client, aclconsumer_key=token, rdf_type="odpt:BusstopPole")
    if not res:
        print("Error: Cant got Stops")
        return
    stops: List[BusstopPole]=res
    print("OK!")
    stops_db={}
    stops_name_db={}
    count=len(stops)
    for i, stop in enumerate(stops):
        print(f"[2/5] Registering Stops... {((i+1)/count)*100:.1f}%\r", end="")
        if args.company not in stop.odptoperator:
            continue
        if stop.dctitle not in stops_name_db:
            try:
                st,_=await Stop.get_or_create(name=stop.dctitle)
            except MultipleObjectsReturned:
                print(f"Warn: Duplicated Stop found: {stop.dctitle}")
                st = await Stop.filter(name=stop.dctitle).first()
            stops_name_db[stop.dctitle]=st
        else:
            st=stops_name_db[stop.dctitle]
        if stop.owlsame_as not in st:
            st.odpt_ids.append(stop.owlsame_as)
        stops_db[stop.owlsame_as]=st
    print("")
    count=len(stops_name_db)
    for i, st in enumerate(stops_name_db.values()):
        print(f"[3/5] Saving changes... {((i+1)/count)*100:.1f}%\r", end="")
        await st.save()
    print("\n[4/5] Getting Lines... ", end="", flush=True)
    lines=await data_dump_operations_dump.asyncio(client=client, aclconsumer_key=token, rdf_type="odpt:BusroutePattern")
    if not lines:
        print("Error: Cant got Lines")
        return
    lines: List[BusroutePattern]
    print("OK!")
    count=len(lines)
    for i, line in enumerate(lines):
        print(f"[5/5] Registering Lines... {((i+1)/count)*100:.1f}%\r", end="")
        if args.company != line.odptoperator:
            continue
        l,_=await Line.get_or_create({"name":line.dctitle, "company":line.odptoperator}, odpt_id=line.owlsame_as)
        for pole in line.odptbusstop_pole_order:
            if not pole.odptbusstop_pole in stops_db:
                print("Line not found:", pole.odptbusstop_pole)
                continue
            await LineStop.get_or_create({"order":pole.odptindex}, line=l, stop=stops_db[pole.odptbusstop_pole])
    print("")
run_async(main())

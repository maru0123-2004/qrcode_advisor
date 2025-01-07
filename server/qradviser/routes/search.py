from ..models.db import Stop
from ..models.response.search import StopData
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=["Search"])

from tortoise.expressions import RawSQL

class L2Distance(RawSQL):
    def __init__(self, field: str, vector: list[float], vector_size: int = 2):
        super().__init__(
            f"({field} <-> "
            f"public.array_to_vector(ARRAY{vector}, {vector_size}, true))"
        )

def findlcs(str1, str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]

    for i, vi in enumerate(str1):
        for j, vj in enumerate(str2):
            if vi == vj:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    return dp[len(str1)][len(str2)]

@router.get("/", response_model=List[StopData])
async def search(search_word: str):
    stops = await Stop.filter(name__contains=search_word)
    stopdatas = [(StopData(stop_id=stop.id, name=stop.name, position=stop.position), findlcs(search_word, stop.name)) for stop in stops]
    stopdatas.sort(key=lambda x:x[1], reverse=True)
    return [i[0] for i in stopdatas]

@router.get("/position", response_model=List[StopData])
async def search_position(lat:float, long:float):
    return [StopData(stop_id=stop["id"], name=stop["name"], position=stop["position"], distance=stop["distance"]) 
            for stop in await Stop.all().annotate(distance=L2Distance(
                "position", vector=[lat,long], vector_size=2
            )).order_by("distance").limit(5).values("id", "name", "position", "distance")
        ]
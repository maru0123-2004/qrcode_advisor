from ..models.db import Stop
from ..models.response.search import StopData
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=["Search"])

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
    stopdatas = [(StopData(stop_id=stop.id, name=stop.name), findlcs(search_word, stop.name)) for stop in stops]
    stopdatas.sort(key=lambda x:x[1], reverse=True)
    return [i[0] for i in stopdatas]
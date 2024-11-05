from ..models.db import Stop
from ..models.response.search import StopData
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=["Search"])

@router.get("/{search_word}", response_model=List[StopData])
async def search(search_word: str):
    stops = await Stop.filter(name__icontains=search_word)
    return [StopData(stop_id=stop.id, name=stop.name) for stop in stops]
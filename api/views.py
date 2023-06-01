from fastapi import APIRouter,status,Response
from .operations import process_orders
from .serializers import Serializer
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache


router = APIRouter()

# Routes
@router.on_event("startup")
async def startup() -> None:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis),prefix="solution-cache")

@router.post("/solution")
@cache(expire=30)
async def solution(data:Serializer) -> Response:
    result = process_orders(data.orders,data.criterion)
    return Response(content=str(result),status_code=status.HTTP_200_OK)



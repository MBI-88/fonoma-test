from fastapi import APIRouter,status,Response
from .operations import process_orders
from .serializers import Serializer


router = APIRouter()

# Routes
@router.post("/solution")
async def solution(data:Serializer) -> Response:
    result = process_orders(data.orders,data.criterion)
    return Response(content=str(result),status_code=status.HTTP_200_OK)
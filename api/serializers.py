from pydantic import BaseModel,Field
from typing import List

class Item(BaseModel):
    id:int = Field(...,ge=0)
    item:str = Field(...,min_length=5)
    quantity:int = Field(...,gt=0)
    price:float = Field(...,gt=0)
    status:str = Field(...,regex="^(completed|canceled|pending)$")


class Serializer(BaseModel):
    orders:List[Item]
    criterion: str = Field(...,regex="^(completed|canceled|pending)$")

    class Config:
        schema_extra = {
            "example":{
                "orders":[
                    {
                        "id":1,
                        "item": "Mac",
                        "quantity":1,
                        "price": 1000.99,
                        "status":"completed"
                    },
                    {
                        "id":2,
                        "item": "Lenovo",
                        "quantity":2,
                        "price": 1500.85,
                        "status":"pending"

                    }
                ],
                "criterion":"completed"
            }
        }
    




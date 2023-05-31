

def process_orders(orders:list, criterion:str) -> float:
    value:float = 0.0
    for item in orders:
        if item.status == criterion:
            value += item.quantity * item.price

    return value
# from fastapi import FastAPI
# from pydantic import BaseModel


# class Product(BaseModel):
#     units: str
#     qty: int

# catalog = {
#     'tomatoes': {
#         'units': 'boxes',
#         'qty': 1000
#     },
#     'wine': {
#         'units': 'bottles',
#         'qty': 500
#     }
# }

# app = FastAPI(title = 'New Jersey API Server')

# @app.get('/warehouse/{product}')
# async def load_truck(product,order_qty):
#     available=catalog[product]['qty']
#     if int(order_qty) > int(available):
#         from fastapi import HTTPException
#         raise HTTPException(
#             status_code=400,
#             detail=f'Sorry, only {available}units are available, please try again...'
#         )

#     catalog[product]['qty'] -= int(order_qty)

#     return {
#         'product': product,
#         'order_qty': order_qty,
#         'units': catalog[product]['units'],
#         'remaining_qty': catalog[product]['qty']
#     }

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel


app = FastAPI()
class Item(BaseModel):
    text: str
    is_done: bool = False

items = []

@app.get('/')
def root():
    return {'Hello:':'World'}

@app.post('/items')
def create_item(item: Item):
    items.append(item)
    return items


@app.get('/items', response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")


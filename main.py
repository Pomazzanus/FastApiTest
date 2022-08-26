from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def root():
    return {"Welcome to our catalog"}

class Restaurants(BaseModel):
    id: int
    name: str
    is_open: bool
    number_of_seats: int
    rating: float


rest_list = []

@app.get('/restaurants')
async def get_restaurants():
    return rest_list


@app.get('/restaurants/{our_rest_id}') #не работает!
async def find_rest(our_rest_id):
    for restaurant in rest_list:
        if rest_list[restaurant["id"]] == our_rest_id:
            return restaurant



@app.post('/restaurants/')
async def add_restaurant(item: Restaurants):
    rest_list.append(item)
    return rest_list



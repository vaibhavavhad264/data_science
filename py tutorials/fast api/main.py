from fastapi import FastAPI
from enum import Enum

app = FastAPI()

food_items = {
    'indian'  : ['Idli',' Dosa'],
    'american' : ['Pizza', 'Hot Dog'],
    'italian' : ['Latte', 'Chocolate Pie']
}

class AvailableCuisines(str, Enum):
    indian  = "indian"
    american = "american"
    italian = "italian"


@app.get("/food_items/{cuisines}")
def get_item(cuisines : AvailableCuisines):
    return food_items.get(cuisines)

@app.get("/hello/{name}")
def hell(name):
    return f"Hello {name}"

@app.get("/")
def hello():
    return "Hello World"


cupon_code = {
    1: "10%",
    2: "20%",
    3: "30%"
}

@app.get("/cupon_code/{code}")
def cupon(code : int):
    return {f"Discount amount : {cupon_code.get(code)}"}
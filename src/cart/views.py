from fastapi import FastAPI

app = FastAPI()
db = {}


@app.get("/cart/{cart_id}")
def cart(cart_id: int):
    return db[cart_id]

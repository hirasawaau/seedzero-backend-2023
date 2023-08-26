from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document

app = FastAPI()


@app.on_event('startup')
async def fastapi_start():
  client = AsyncIOMotorClient("mongodb://localhost:27017")
  await init_beanie(client.seedzero_lunch, document_models=[FoodModel])


class Food(BaseModel):
  title: str
  ingredients: List[str]


class FoodModel(Document):
  title: str
  ingredients: List[str]


@app.post('/foods', status_code=201)
async def create_food(f: Food) -> FoodModel:
  doc = FoodModel(
    title=f.title,
    ingredients=f.ingredients
  )

  await doc.insert()
  return doc


@app.get('/foods')
async def get_foods():
  docs = await FoodModel.find().to_list()
  return docs


@app.get('/foods/{id}')
async def get_food(id: str):
  try:
    doc = await FoodModel.get(id)
    if doc is None:
      raise ValueError("Value is None")
    return doc
  except:
    raise HTTPException(status_code=404, detail="Not found")


@app.delete('/foods/{id}', status_code=204)
async def delete_food(id: str):
  try:
    doc = await FoodModel.get(id)
    await doc.delete()
  except:
    raise HTTPException(status_code=404, detail="Not found")


@app.put('/foods/{id}')
async def replace_food(id: str, f: Food):
  try:
    doc = await FoodModel.get(id)
    if doc is None:
      raise ValueError("Value is None")
    doc.title = f.title
    doc.ingredients = f.ingredients

    await doc.save()
    return doc
  except:
    raise HTTPException(status_code=404, detail="Not found")


@app.get('/hello/{msg}')
def hello_world(msg: str, body: Food, a: Optional[int] = None) -> dict:
  return {
    "food_title": body.title,
    "ingredients": body.ingredients
  }

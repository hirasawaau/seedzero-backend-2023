from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document

app = FastAPI()

class ProfileDoc(Document):
  name: str
  surname: str
  age: int | None = None

class Profile(BaseModel):
  name: str
  surname: str
  age: int | None = None
  
@app.on_event('startup')
async def fastapi_start():
  client = AsyncIOMotorClient('mongodb://localhost:27017')
  await init_beanie(client.breakfast , document_models=[ProfileDoc])


@app.post('/profiles')
async def create_profile(pf: Profile) -> ProfileDoc:
  doc = ProfileDoc(
    name=pf.name,
    surname=pf.surname,
    age=pf.age
  )

  await doc.insert()
  return doc

@app.get('/profiles')
async def get_profiles():
  docs = await ProfileDoc.find().to_list()
  return docs

@app.get('/profiles/{id}')
async def get_profile(id: str):
  doc = await ProfileDoc.get(id)
  return doc

@app.delete('/profiles/{id}')
async def delete_profile(id: str):
  doc = await ProfileDoc.get(id)
  await doc.delete()
  return doc

@app.put('/profiles/{id}')
async def replace_profile(id: str , pf: Profile):
  doc = await ProfileDoc.get(id)
  doc.name = pf.name
  doc.surname = pf.surname
  doc.age = pf.age
  await doc.save()

  return doc
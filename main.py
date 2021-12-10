from fastapi import FastAPI, Query
import aioredis
from anogram import Anogram_check
import aioredis

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'Thanks for giving me an oppotunity to share myself'}

@app.get("/isanogram")
async def isanogram(q: str = Query(None), q2: str = Query(None)):
    a = await counter()
    return  Anogram_check(q, q2,a)



@app.get("/redis")
async def counter():

    redis = aioredis.from_url("redis://localhost/0")
    value = await redis.get("counter")
    await redis.set("counter", int(value)+1)
    print(redis)
    return(value)
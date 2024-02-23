import azure.functions as func

import random

import fastapi

app = fastapi.FastAPI()

@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/<your name> for parameterized route.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }

@app.get("/randomnum")
def randomnum():
  randNum = random.randint(1,1000) 
  return {'Here is a random number between 1 and 1000: ' + str(randNum) + '!'}
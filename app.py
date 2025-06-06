#from flask import Flask, request
#from flask_cors import CORS

from fastapi import FastAPI, status
import uvicorn

import json
import mockup
from contextlib import asynccontextmanager

import os
from dotenv import load_dotenv

from typing import Union

load_dotenv()

import dbHandlers.dbhandler as handler

from dbHandlers.models import GameDetails

# import pymongo

# Check how to split into files for routes maybe?

def generic_mockup(mockup_string):
    response = json.loads(mockup_string)
    return response

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code before ; inits
    await handler.init_database()
    yield #This is when server is running
    # Code after ; dallocs


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return "This is the server root"

@app.get("/game", status_code=status.HTTP_200_OK)
async def get_all_games(user_id: Union[str, None] = None):
    if user_id:
        print("User Query Parameter provided: ", user_id)
        gameObj = await handler.get_multiple_from_collection({"gameOwnerId": user_id}) #Recheck sometime
    else:
        gameObj = await handler.get_multiple_from_collection()
    print(gameObj)
    return gameObj

@app.get("/game/{game_id}", status_code=status.HTTP_200_OK)
async def get_game_by_id(game_id):
    print(game_id)
    gameObj = await handler.get_from_collection(game_id)
    print(gameObj)
    return gameObj

@app.post("/game", status_code=status.HTTP_201_CREATED)
async def post_one_game(game: GameDetails):
    result = await game.insert()
    return result

@app.put("/game", status_code=status.HTTP_201_CREATED)
async def put_one_game(game: GameDetails):
    result = await game.replace()
    return result

@app.patch("/game", status_code=status.HTTP_201_CREATED)
async def patch_one_game(game: GameDetails):
   document_dict = {}
   for key, value in game.model_dump().items():
       if value is not None:
           document_dict[key] = value
   result = await game.update({'$set': document_dict})

@app.delete("/game/{game_id}", status_code=status.HTTP_200_OK)
async def delete_one_game(game_id):
    game = await GameDetails.get(game_id)
    print(game)
    await game.delete()
    return {}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
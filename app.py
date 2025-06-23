#from flask import Flask, request
#from flask_cors import CORS

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import json
import mockup
from contextlib import asynccontextmanager

import os
from dotenv import load_dotenv

from typing import Union

load_dotenv()

import dbHandlers.dbhandler as handler

from dbHandlers.models import GameDetails, LinkTest

from beanie import Link, WriteRules, PydanticObjectId

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

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

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

@app.post("/listing", status_code=status.HTTP_201_CREATED)
async def post_one_listing(listing: LinkTest):
    print(listing.testId)
    if listing.testId:
        print(listing.testId)
        game = GameDetails.link_from_id(PydanticObjectId(listing.testId))
        print(game, "NEXT")
        listing.testLink = game
        print(listing.testLink, " NEXT ")
        print(listing)
        result = await listing.insert()

@app.get("/listing/{listing_id}")
async def get_one_listing(listing_id):
    listing = await LinkTest.get(listing_id, fetch_links=True, nesting_depth=1)
    print(listing.testLink)
    return listing

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
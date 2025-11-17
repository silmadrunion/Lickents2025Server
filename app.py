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

#import dbHandlers.dbhandler as handler
from models.handler import init_database
from routes import game, listing

#from dbHandlers.models import GameDetails, ListingDetails, ListingObject

from beanie import Link, WriteRules, PydanticObjectId

# import pymongo

# Check how to split into files for routes maybe?

def generic_mockup(mockup_string):
    response = json.loads(mockup_string)
    return response

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code before ; inits
    await init_database()
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
    allow_methods = ["*"],
    allow_headers = ["*"],
    expose_headers=["*"]
)

app.include_router(game.router)
app.include_router(listing.router)

@app.get("/")
async def root():
    return "This is the server root"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
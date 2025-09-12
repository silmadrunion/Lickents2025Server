from models.game import GameDetails
from models.listing import ListingDetails

from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie

import os
from dotenv import load_dotenv

uri = os.environ['MONGO_CONNECTION_STRING']


async def init_database():
    client = AsyncIOMotorClient(uri)

    await init_beanie(database=client.LicentaGamesDB, document_models=[ListingDetails, GameDetails])

    print("DB Initialized")
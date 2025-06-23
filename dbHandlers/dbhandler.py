import pymongo
import asyncio
from beanie import Document, Indexed, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from dbHandlers.models import GameDetails, GameObject, UserDetails, LinkTest

import os
from dotenv import load_dotenv


# Make into a singleton to import in other modules

# Possibly deprecate once the User Details db entity has been made

default_details = UserDetails()
print(default_details)

uri = os.environ['MONGO_CONNECTION_STRING']

async def init_database():
    client = AsyncIOMotorClient(uri)

    await init_beanie(database=client.LicentaGamesDB, document_models=[GameDetails, LinkTest])

    print("DB Initialized")

async def get_from_collection(object_id):

    result = 0

    print(object_id)
    result = await GameDetails.get(object_id)

    print("DB RESULT:", result)

    game_object = GameObject(gameUserDetails = default_details, gameDetails = result)
    #game_object = TestModel(test = default_details)
    print(game_object)

    return game_object

async def get_multiple_from_collection(query = {}):

    result = 0

    print(query)
    result = await GameDetails.find(query).to_list()

    print("DB RESULT:", result)

    for item in result:
        item = GameObject(gameUserDetails=default_details, gameDetails=item)

    print(result)

    return result


'''
Kept for future possible reference

def insert_to_collection(collection_name, object_dict, object_id = None, patch=False):
    if collection_name in collections:
        if object_id:
            if patch:
                result = collections[collection_name].update_one({"_id":ObjectId(object_id)}, {'$set': object_dict}, upsert=True)
            else:
                result = collections[collection_name].replace_one({"_id":ObjectId(object_id)},object_dict)
        else:
            result = collections[collection_name].insert_one(object_dict)
        return result
    else:
        return False # Error handling ??
 
#    print(result.acknowledged) # Boolean of if it worked
#    print(result.inserted_id) # String of the inserted ID

'''
import pymongo
import asyncio
from beanie import Document, Indexed, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from dbHandlers.models import GameDetails

import os
from dotenv import load_dotenv


# Make into a singleton to import in other modules


'''collections = {
    "Games": database["Games"]
}
'''

uri = os.environ['MONGO_CONNECTION_STRING']

async def get_from_collection(object_id):
    client = AsyncIOMotorClient(uri)

    await init_beanie(database=client.LicentaGamesDB, document_models=[GameDetails])

    result = 0

    print(object_id)
    result = await GameDetails.get(object_id)

    #print("DB RESULT:", result)

    return result

'''
try: 
    client = pymongo.MongoClient(uri, server_api=pymongo.server_api.ServerApi(version="1", strict=True, deprecation_errors=True))

    client.admin.command("ping")
    print("Successfully connected to database!")



    database = client["LicentaGamesDB"]


except Exception as e:
    raise Exception("Error connecting to database: ", e)

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

        
def get_from_collection(collection_name, object_id):
    if collection_name in collections:
        #result = collections[collection_name].find_one({"_id": ObjectId(object_id)},{"_id": {"$toString": "$_id"}})
        pipeline = [
                { "$match": { "_id": ObjectId(object_id) } },
                { "$addFields": { "_id": { "$toString": "$_id" } } }
                    ]
        result = collections[collection_name].aggregate(pipeline).next()
        print(result)
        return result
    else:
        return False # Error handle

def get_multiple_from_collection(collection_name, query = {}):
    if collection_name in collections:
        pipeline = [
                { "$match": query },
                { "$addFields": { "_id": { "$toString": "$_id" } } }
                    ]
        result = collections[collection_name].aggregate(pipeline)
        return list(result)
    else:
        return False # Error handle

def delete_from_collection(collection_name, object_id):
    if collection_name in collections:
        result = collections[collection_name].delete_one({"_id":ObjectId(object_id)})
    return result
    '''
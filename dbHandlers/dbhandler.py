import pymongo
from bson import ObjectId

import os
from dotenv import load_dotenv


# Make into a singleton to import in other modules




uri = os.environ['MONGO_CONNECTION_STRING']


try: 
    client = pymongo.MongoClient(uri, server_api=pymongo.server_api.ServerApi(version="1", strict=True, deprecation_errors=True))

    client.admin.command("ping")
    print("Successfully connected to database!")



    database = client["LicentaGamesDB"]

    collections = {
    "Games": database["Games"]
}

except Exception as e:
    raise Exception("Error connecting to database: ", e)

def insert_to_collection(collection_name, object_dict, object_id = None):
    if collection_name in collections:
        if object_id:
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
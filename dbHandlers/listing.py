import dbHandlers.dbhandler as dbhandler
import dbHandlers.validators as validators

import dbHandlers.game as game

from bson import ObjectId

import json

# Lambda Notes 
# x = lambda a: True if a > 10 else False
# x = lambda a: True if a is not None else False
# x = lambda a, conditional: False if a is None else (False if conditional(a) else True)
# x = lambda a: isinstance(a, str)
# x = lambda a: True if 'key' in dict else False

#Leftover for historical reasons for now, will delete in the future


temp_hardcoded_user_dict = {
        "_id": "stri123123123ng",
        "gameUserRating": 4.99,
        "gameUserName": "Fluff Robota",
        "gameUserImagePath": "some path"
        }

class Listing:
    def __init__(self): # will be formed as a default empty shell, and is only settable through its setters
        self.dict = {}

    # This will need to also validate that no extra keys exist, implement a key list check for that
    def validateObject(self, inputDict):
        error_log = []
        if not "gameId" in inputDict:
            error_log.append("gameId is missing")
        elif not isinstance(inputDict["gameId"], str):
            error_log.append("gameId is not String")

    def set_from_api(self, inputMultiDict): # This will run validation eventually
        self.dict = inputMultiDict.to_dict() # Listing won't require Game Details when populated from API, as an fk is all the Post and Patch require

    def set_from_db(self, db_id): # This will fetch from db by id into self.dict
        #return error if not string
        self.dict = dbhandler.get_from_collection("Listings", db_id)

        self.dict["gameDetails"] = dbhandler.get_from_collection("Games", self.dict["gameId"])

        if len(self.dict["offerIds"]) > 0: # See about rewriting this with a multi ID aggregate straight from DB
            self.dict["offers"] = []
            for offerId in self.dict["offerIds"]:
                self.dict["offers"].append(dbhandler.get_from_collection("Offers", offerId))


    def get_dict(self):
        return self.dict
    
    def set_multiple_dicts(self, user_id=None):
        if user_id:
            self.dict = dbhandler.get_multiple_from_collection("Games", {"gameOwnerId": user_id}) # Recheck this
        else:
            self.dict = dbhandler.get_multiple_from_collection("Games")

        for game in self.dict:
            game["gameUserDetails"] = temp_hardcoded_user_dict
        print(self.dict)

    
    def upload_to_db(self, object_id=None):
        
        result = dbhandler.insert_to_collection("Games", self.dict, object_id)

        if result.acknowledged:
            if object_id:
                return str(result.upserted_id)
            else:
                return str(result.inserted_id)
        else:
            return f"Error? {result}"
        
    def delete_from_db(self,object_id):
        result = dbhandler.delete_from_collection("Games", object_id)

        if result.acknowledged:
            return str(result.deleted_count)
        else:
            return f"Error? {result}"
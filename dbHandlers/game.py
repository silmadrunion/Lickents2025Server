import dbHandlers.dbhandler as dbhandler
import dbHandlers.validators as validators

from bson import ObjectId

import json

import werkzeug.datastructures

# Lambda Notes 
# x = lambda a: True if a > 10 else False
# x = lambda a: True if a is not None else False
# x = lambda a, conditional: False if a is None else (False if conditional(a) else True)
# x = lambda a: isinstance(a, str)
# x = lambda a: True if 'key' in dict else False


temp_hardcoded_user_dict = {
        "_id": "stri123123123ng",
        "gameUserRating": 4.99,
        "gameUserName": "Fluff Robota",
        "gameUserImagePath": "some path"
        }

class Game:
    def __init__(self): # will be formed as a default empty shell, and is only settable through its setters
        self.dict = {}

    # This will need to also validate that no extra keys exist, implement a key list check for that
    def validateObject(self, inputDict):
        error_log = []
        if not "gameId" in inputDict:
            error_log.append("gameId is missing")
        elif not isinstance(inputDict["gameId"], str):
            error_log.append("gameId is not String")

    def set_from_api(self, input): # This will run validation eventually
        self.dict = input

    def set_from_db(self, db_id): # This will fetch from db by id into self.dict
        #return error if not string
        self.dict = {}

        self.dict["gameDetails"] = dbhandler.get_from_collection("Games", db_id)

        self.dict["gameUserDetails"] = temp_hardcoded_user_dict

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

    
    def upload_to_db(self, object_id=None, patch=False):
        print("ID:", object_id)
        result = dbhandler.insert_to_collection("Games", self.dict, object_id, patch)

        print(result)

        if result.acknowledged:
            if object_id:
                new_id = object_id
            else:
                new_id = str(result.inserted_id)

            self.set_from_db(new_id)

            print(self.dict)

            return self.dict
        
        else:
            return f"Error? {result}"
        
    def delete_from_db(self,object_id):
        result = dbhandler.delete_from_collection("Games", object_id)

        if result.acknowledged:
            return str(result.deleted_count)
        else:
            return f"Error? {result}"
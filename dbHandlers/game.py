import dbHandlers.dbhandler as dbhandler
import dbHandlers.validators as validators

from bson import ObjectId

import json

# Lambda Notes 
# x = lambda a: True if a > 10 else False
# x = lambda a: True if a is not None else False
# x = lambda a, conditional: False if a is None else (False if conditional(a) else True)
# x = lambda a: isinstance(a, str)
# x = lambda a: True if 'key' in dict else False



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

    def set_from_api(self, inputMultiDict): # This will run validation eventually
        self.dict = inputMultiDict.to_dict()

    def set_from_db(self, db_id): # This will fetch from db by id into self.dict
        #return error if not string
        self.dict = dbhandler.get_from_collection("Games", db_id)

    def get_dict(self):
        return self.dict
    
    def set_multiple_dicts(self, user_id=False):
        if user_id:
            self.dict = dbhandler.get_multiple_from_collection("Games", {"gameOwnerId": user_id}) # Recheck this
        else:
            self.dict = dbhandler.get_multiple_from_collection("Games")
            print(self.dict)

    
    def upload_to_db(self):
        result = dbhandler.insert_to_collection("Games", self.dict)

        if result.acknowledged:
            return str(result.inserted_id)
        else:
            return f"Error? {result}"
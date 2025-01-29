import pymongo

class dbhandler:
    
    def __init__(self, connection_string):
        self.client = pymongo.MongoClient(connection_string, server_api=pymongo.server_api.ServerApi(version="1", strict=True, deprecation_errors=True))
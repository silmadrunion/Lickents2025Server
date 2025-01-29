from flask import Flask
from flask_cors import CORS

from requests import request
import json
import mockup


import os
from dotenv import load_dotenv

import pymongo


load_dotenv()


app = Flask(__name__)
CORS(app)

def generic_mockup(mockup_string):
    response = json.loads(mockup_string)
    return response

try:
    uri = os.environ['MONGO_CONNECTION_STRING']
    db_client = pymongo.MongoClient(uri, server_api=pymongo.server_api.ServerApi(
    version="1", strict=True, deprecation_errors=True))


    database = db_client["LicentaGamesDB"]

    collection = database["Games"]

    db_client.admin.command("ping")

    
    object_dict = {}
    object_dict['game_id'] = 12345
    object_dict['game_name'] = 'testName'
    object_dict['game_description'] = 'testDescription'

    print(object_dict)

    result = collection.insert_one(object_dict) #Using Dumps not Jsonify because we do not need the extra response-type data jsonify provides
    print(result.acknowledged) # Boolean of if it worked
    print(result.inserted_id) # String of the inserted ID

    print(result)

    print("Connected successfully to database") # Investigate, should this stay open, or should I reopen it every time I do a route?

except Exception as e:
    raise Exception("Error!! ", e)


@app.route("/", methods=['GET'])
def hello_world():
    return "Response"

@app.route("/listings", methods=['GET', 'POST', 'PUT', 'DELETE'])
def mock_get_listings():

    if request.method == 'GET':
        game_id = request.args.get('game-id')
        if game_id:
            return generic_mockup(mockup.single_listing)
        else:
            return generic_mockup(mockup.all_listings)
    if request.method == 'POST':
        game_id = request.form.get('game_id')


    if request.method == 'PUT':
        game_id = request.args.get('game-id')

    if request.method == 'DELETE':
        game_id = request.args.get('game-id')
        return "Deleted"

@app.route("/listing", methods=['GET'])
def mock_get_listing():
    return generic_mockup(mockup.single_listing)

@app.route("/games-library", methods=['GET'])
def mock_get_library():
    client_id = request.args.get('client-id')
    if client_id:
        return generic_mockup()
    else:
        return "ERROR"
    
@app.route("/games", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_game():
    if request.method == 'GET':
        game_id = request.args.get('game-id')
        if game_id:
            return "single game"
        else:
            return "all games"
    if request.method == 'POST': # build a smarter way to do this than by hand

        object_dict = {}
        object_dict.game_id = request.form.get('gameOwnerId')
        object_dict.game_name = request.form.get('gameName')
        object_dict.game_description = request.form.get('gameDescription')

        result = collection.insert_one(json.jsonify(object_dict))

        print(result)



    if request.method == 'PUT':
        game_id = request.args.get('game-id')

    if request.method == 'DELETE':
        game_id = request.args.get('game-id')
        return "Deleted"

    return "error"


# This is a working connection example, look to setup DB next
""" try:
    uri = os.environ['MONGO_CONNECTION_STRING']
    client = pymongo.MongoClient(uri, server_api=pymongo.server_api.ServerApi(
    version="1", strict=True, deprecation_errors=True))

    client.admin.command("ping")

    print("Connected successfully")

    client.close()

except Exception as e:
    raise Exception("Error!! ", e)"""
from flask import Flask, request
from flask_cors import CORS

import json
import mockup


import os
from dotenv import load_dotenv

# import pymongo


load_dotenv()


app = Flask(__name__)
CORS(app)

def generic_mockup(mockup_string):
    response = json.loads(mockup_string)
    return response
"""
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
"""

@app.route("/", methods=['GET'])
def hello_world():
    return "Response"

@app.route("/game", methods=['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def mock_get_games():

    if request.method == 'GET':
        game_id = request.args.get('game-id')
        user_id = request.args.get('user-id')  # requires all games by user id, currently just catching it for mockup
        if game_id:
            return generic_mockup(mockup.single_game)
        else:
            return generic_mockup(mockup.all_games) 
    if request.method == 'POST':
        game_id = request.form.get('game-id')
        game_name = request.form.get('game-name') # Find a smarter way to process because this will be the entire obj cast line by line otherwise

        return generic_mockup(mockup.game_post)


    if request.method == 'PUT': # this is here for classic REST support, might remove it in the final version as PATCH handles the Update in CRUD
        game_id = request.args.get('game-id')
        game_name = request.form.get('game-name')

        return generic_mockup(mockup.game_put)

    if request.method == 'PATCH':
        game_id = request.args.get('game-id')
        game_name = request.form.get('game-name')

        return generic_mockup(mockup.game_patch)


    if request.method == 'DELETE':
        game_id = request.args.get('game-id')
        return generic_mockup(mockup.deleted_empty) #only because returning empty json might not be that straight and I don't wanna find out

@app.route("/listing", methods=['GET', 'POST', 'PUT', 'DELETE'])
def mock_get_listings():

    if request.method == 'GET':
        listing_id = request.args.get('listing-id')
        user_id = request.args.get('user-id')
        if listing_id:
            return generic_mockup(mockup.single_listing)
        else:
            return generic_mockup(mockup.all_listings)
        
    if request.method == 'POST':
        game_id = request.form.get('game-id')

        return generic_mockup(mockup.listing_post)

    if request.method == 'PUT':
        game_id = request.args.get('game-id')

        return generic_mockup(mockup.listing_put)

    if request.method == 'PATCH':
        game_id = request.args.get('game-name')

        return generic_mockup(mockup.listing_patch)

    if request.method == 'DELETE':
        listing_id = request.args.get('listing-id')
        return generic_mockup(mockup.deleted_empty)
    
@app.route("/offer", methods=['GET', 'POST', 'PUT', 'DELETE'])
def mock_get_offers():

    if request.method == 'GET':
        offer_id = request.args.get('offer-id')
        user_id = request.args.get('user-id')
        if offer_id:
            return generic_mockup(mockup.single_offer)
        else:
            return generic_mockup(mockup.all_offers)
        
    if request.method == 'POST':
        game_id = request.form.get('game-id')
        listing_id = request.form.get('listing-id')

        return generic_mockup(mockup.offer_post)

    if request.method == 'PUT':
        offer_id = request.args.get('offer-id')
        game_id = request.form.get('game-id')

        return generic_mockup(mockup.offer_put)

    if request.method == 'PATCH':
        offer_id = request.args.get('offer-id')
        game_id = request.form.get('game-id')

        return generic_mockup(mockup.offer_patch)

    if request.method == 'DELETE':
        offer_id = request.args.get('offer-id')
        return generic_mockup(mockup.deleted_empty)
    



""" 
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
"""

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
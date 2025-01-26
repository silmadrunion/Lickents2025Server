from flask import Flask
from requests import request
import json
import mockup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generic_mockup(mockup_string):
    response = json.loads(mockup_string)
    return response

@app.route("/", methods=['GET'])
def hello_world():
    return "Response"

@app.route("/listings", methods=['GET'])
def mock_get_listings():
    return generic_mockup(mockup.all_listings)

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
    

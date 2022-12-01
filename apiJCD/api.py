from flask import Flask
from flask_cors import CORS
from parser import Client

from conf import TOKEN

client = Client(TOKEN)

app = Flask(__name__)
CORS(app)
@app.route('/')
def homepage():
    return "Hello world !"

@app.route('/contracts')
def contracts():
    return {'items': [contract for contract in client.contracts()]}

@app.route('/stations')
def stations():
    return {'items': [station for station in client.stations()]}

@app.route('/contracts/<contract>/stations')
def contractliststations(contract):
    return {'items': [station for station in client.contract_liststations(contract)]}

@app.route('/contracts/<contract>/stations/<station_number>')
def contracstation(contract, station_number):
    return client.contract_station(contract, station_number)
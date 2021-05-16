from flask import Flask
from flask_restful import Api
from .resources.equipment import Equipment
from .resources.status import Status
from .resources.vessel import Vessel
from .resources.vessellist import VesselList


app = Flask(__name__)
api = Api(app)



api.add_resource(VesselList, '/vessels')
api.add_resource(Vessel, '/vessel/<string:code>')
api.add_resource(Equipment, '/equipment/<string:code>')
# api.add_resource(Status, '/status/<string:code>')
api.add_resource(Status, '/status')


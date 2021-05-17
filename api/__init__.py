from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from .resources.mandatory.equipment import Equipment
from .resources.mandatory.status import Status
from .resources.mandatory.vessel import Vessel
from .resources.mandatory.vessels import Vessels
from .resources.extra.list_equipments import ListEquipments
from .resources.extra.list_vessels import ListVessels


app = Flask(__name__)
api = swagger.docs(Api(app),apiVersion='1.0',api_spec_url='/docs')


# Mandatory endpoints
api.add_resource(Vessels, '/vessels')
api.add_resource(Vessel, '/vessel/<string:code>')
api.add_resource(Equipment, '/equipment/<string:code>')
api.add_resource(Status, '/status')

# Extra endpoints
api.add_resource(ListVessels, '/listvessels')
api.add_resource(ListEquipments, '/listequipaments')

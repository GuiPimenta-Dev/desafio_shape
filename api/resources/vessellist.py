from ..db.conn import ConnectToDatabase
from flask_restful import Resource,request

class VesselList(Resource,ConnectToDatabase):
    def get(self):
        
        objects = []
        for object in self.collection_vessels.find({},{"_id":0}):
            objects.append(object)

        return {'data': objects }, 200

    def post(self):

        args = request.form
        if self.collection_vessels.find_one({'code': args['code']}):
            return {'message': 'This Vessel is already registered'}, 400

        else:
            vessel = {'code':args['code']}
            self.collection_vessels.insert(vessel)
            return {'message': f'Vessel {args["code"]} registered'}, 201
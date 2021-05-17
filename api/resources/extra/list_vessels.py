from ...db.conn import ConnectToDatabase
from flask_restful import Resource
from flask_restful_swagger import swagger


class ListVessels(Resource,ConnectToDatabase):
    @swagger.model
    @swagger.operation(notes='List all vessels') 
    def get(self):            
            objects = []
            for object in self.collection_vessels.find({},{"_id":0}):
                objects.append(object)

            return {'data': objects }, 200
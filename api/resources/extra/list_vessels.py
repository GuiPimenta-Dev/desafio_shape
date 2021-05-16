from ...db.conn import ConnectToDatabase
from flask_restful import Resource, request

class ListVessels(Resource,ConnectToDatabase): 
    def get(self):            
            objects = []
            for object in self.collection_vessels.find({},{"_id":0}):
                objects.append(object)

            return {'data': objects }, 200
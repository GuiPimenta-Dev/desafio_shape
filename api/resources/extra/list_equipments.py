from ...db.conn import ConnectToDatabase
from flask_restful import Resource
from flask_restful_swagger import swagger


class ListEquipments(Resource,ConnectToDatabase): 
    @swagger.model
    @swagger.operation(notes='some notes')
    def get(self):            
            objects = []
            for object in self.collection_equipments.find({},{"_id":0}):
                objects.append(object)

            return {'data': objects }, 200
from flask_restful_swagger import swagger
from ...db.conn import ConnectToDatabase
from flask_restful import Resource
from ...constants.status import StatusEnum
from flask_restful_swagger import swagger


class Vessel(Resource,ConnectToDatabase):    
    @swagger.model
    @swagger.operation(notes='List all active equipments of a vessel',parameters=[
            {
              "name": "code",
              "description": "Vessel code to list active equipments",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "path"
            }
            ] 
            )
    def get(self, code):       
        
        if not self.collection_vessels.find_one({'code': code}):
            return {'message': 'Vessel not found'}, 404

        objects = []
        for object in self.collection_equipments.find({'vessel': code , 'status': StatusEnum.ACTIVE }, {"_id": 0}):            
            objects.append(object)

        if objects:
            return {
                    'message': f'Vessel {code} contains active equipments',
                    'data': objects
                    }, 200 
        else:
            return {},204

from flask_restful_swagger import swagger
from ...db.conn import ConnectToDatabase
from flask_restful import Resource
from ...constants.status import StatusEnum
from flask_restful_swagger import swagger


class Vessel(Resource,ConnectToDatabase):    
    @swagger.model
    @swagger.operation(notes='List all active equipments of a vessel')
    def get(self, vessel):       
        
        if not self.collection_vessels.find_one({'code': vessel}):
            return {'message': 'Vessel not found'}, 404

        objects = []
        for object in self.collection_equipments.find({'vessel': vessel , 'status': StatusEnum.ACTIVE }, {"_id": 0}):            
            objects.append(object)

        if objects:
            return {
                    'message': f'Vessel {vessel} contains active equipments',
                    'data': objects
                    }, 200 
        else:
            return {},204

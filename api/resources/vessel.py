from ..db.conn import ConnectToDatabase
from flask_restful import Resource
from ..constants.status import StatusEnum

class Vessel(Resource,ConnectToDatabase):
    def get(self, code):

        if not self.collection_vessels.find_one({'code': code}):
            return {'message': 'Vessel not found'}, 404

        objects = []
        for object in self.collection_equipments.find({'vessel': code , 'status': StatusEnum.ACTIVE }, {"_id": 0}):
            objects.append(object)

        return {'data': objects}, 200

    
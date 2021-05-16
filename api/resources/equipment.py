from ..db.conn import ConnectToDatabase
from flask_restful import Resource, request
from ..constants.status import StatusEnum

class Equipment(Resource,ConnectToDatabase):

    def post(self, code):


        if not self.collection_vessels.find_one({'code': code}):
            return {'message': 'Vessel not found'}, 404
        else:
            args = request.form

            if self.collection_equipments.find_one({"code": args['code']}):
                return {'message': f'The equipment code must be unique'}, 400
            else:
                equipment = {
                                "vessel": code,
                                "code": args['code'],
                                "name": args['name'],
                                "location": args['location'],
                                "status": StatusEnum.ACTIVE
                            }

                self.collection_equipments.insert(equipment)

                return {'data': f'The equipment {args["code"]} was registered'} , 200
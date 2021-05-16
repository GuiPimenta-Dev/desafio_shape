from ...db.conn import ConnectToDatabase
from flask_restful import Resource, request
from ...constants.status import StatusEnum


class Equipment(Resource,ConnectToDatabase):   
    def post(self, code):

        args = request.form

        if not 'code' in args:
            return {'message': 'Equipment code is required'}, 400     

        elif not args['code']:
            return {'message': 'Equipment code can`t be null'}, 400

        
        if not 'name' in args:
            return {'message': 'Equipment name is required'}, 400

        elif not args['name']:
            return {'message': 'Equipment name can`t be null'}, 400

        
        if not 'location' in args:
            return {'message': 'Equipment location is required'}, 400

        elif not args['location']:
            return {'message': 'Equipment location can`t be null'}, 400


        if not self.collection_vessels.find_one({'code': code}):
            return {'message': 'Vessel not found'}, 404
  
        else:
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

                del equipment['_id']

                return {
                        'message': f'Equipment {args["code"]} created successfully',
                        'data': equipment
                        } , 201
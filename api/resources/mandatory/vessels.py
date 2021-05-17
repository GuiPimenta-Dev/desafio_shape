from ...db.conn import ConnectToDatabase
from flask_restful import Resource,request
from flask_restful_swagger import swagger


class Vessels(Resource,ConnectToDatabase):
    @swagger.model
    @swagger.operation(
    notes='Create new vessels',
        parameters=[
            {
              "name": "code",
              "description": "Unique code for vessel",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "form"
            }
          ]
        )
    def post(self):
        args = request.form

        if not 'code' in args:
            return {'message': 'Vessel code is required'}, 400            
        elif not args['code']:
            return {'message': 'Vessel code can`t be null'}, 400

        if self.collection_vessels.find_one({'code': args['code']}):            
            return {'message': 'This Vessel is already registered'}, 400

        else:
            vessel = {'code':args['code']}
            self.collection_vessels.insert(vessel)

            del vessel['_id']
            
            return { 
                    'message': f'Vessel {args["code"]} created successfully',
                    'data': vessel
                    }, 201
from ...db.conn import ConnectToDatabase
from flask_restful import Resource,request
from ...constants.status import StatusEnum
from flask_restful_swagger import swagger 
    

class Status(Resource,ConnectToDatabase):
    @swagger.model
    @swagger.operation(
    notes='Change equipment status',
        # parameters=[
        #     {
        #       "name": "code",
        #       "description": "list of equipment codes separated by commas",
        #       "required": True,
        #       "allowMultiple": False,
        #       "paramType": "query"
        #     }
        #   ]
        )
    def get(self):
        if not request.args:
            return {"message": 'Query params missing'}, 400

        if not request.args['code']:
            return {"message": 'Code param is missing'}, 400
        

        code_log = {}
        codes = request.args['code'].split(',')            
        for code in codes:
            if not self.collection_equipments.find_one({"code": code}):
                code_log[code]={'message': f'Equipment {code} not found','status': 404}
                
            else:

                if self.collection_equipments.find_one({"code": code,'status': StatusEnum.ACTIVE}):
                    self.collection_equipments.update({"code": code },{"$set": {'status': StatusEnum.INACTIVE}} )
                    data = self.collection_equipments.find_one({"code": code},{'_id': 0})

                    code_log[code]={
                                    'message': f'Equipment {code} is inactive', 
                                    'data': data ,
                                    'status': 200
                                    }
                else:
                    self.collection_equipments.update({"code": code }, {"$set": {'status': StatusEnum.ACTIVE}})                    
                    data = self.collection_equipments.find_one({"code": code},{'_id': 0})

                    code_log[code]={
                                    'message': f'Equipment {code} is active', 
                                    'data': data ,
                                    'status': 200
                                    }
                                  
        
        return code_log, 200


  
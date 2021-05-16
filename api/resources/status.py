from ..db.conn import ConnectToDatabase
from flask_restful import Resource,request
from ..constants.status import StatusEnum


class Status(Resource,ConnectToDatabase):
    def get(self):
        if not request.args:
            return {"message": 'Query params missing'}, 400

        if not request.args['code']:
            return {"message": 'Key code was not informed'}, 400


        code_log = {}
        codes = request.args['code'].split(',')            
        for code in codes:
            if not self.collection_equipments.find_one({"code": code}):
                code_log[code]={'message': 'Equipment not found','status': 404}
                
            else:
                if self.collection_equipments.find_one({"code": code,'status': StatusEnum.ACTIVE}):
                    self.collection_equipments.update({"code": code },{"$set": {'status': StatusEnum.INACTIVE}} )
                    code_log[code]={'message': 'Equipment is inactive', 'status': 200}
                else:
                    self.collection_equipments.update({"code": code }, {"$set": {'status': StatusEnum.ACTIVE}})
                    code_log[code]={'message': 'Equipment is active', 'status': 200}
                                  
        
        return code_log, 200


  
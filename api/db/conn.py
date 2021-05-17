import pymongo
import os
# from env import USER,PASS,DB,RETRY,VESSELS,EQUIPMENTS

class ConnectToDatabase():
#     conn = pymongo.MongoClient(
#         f"mongodb+srv://{USER}:{PASS}@backend.lwkqa.mongodb.net/{DB}?retryWrites={RETRY}&w=majority")

    conn = pymongo.MongoClient(
            f"mongodb+srv://{os.environ['USER']}:{os.environ['PASS']}@backend.lwkqa.mongodb.net/{os.environ['DB']}?retryWrites={os.environ['RETRY']}&w=majority")


    db = conn.desafio_shape

#     collection_vessels = db[VESSELS]
#     collection_equipments = db[EQUIPMENTS]
    collection_vessels = db[os.environ['VESSELS']]
    collection_equipments = db[os.environ['EQUIPMENTS']]
import pymongo
from .env import USER,PASS,DB,RETRY,VESSELS,EQUIPMENTS

class ConnectToDatabase():
    conn = pymongo.MongoClient(
        f"mongodb+srv://{USER}:{PASS}@backend.lwkqa.mongodb.net/{DB}?retryWrites={RETRY}&w=majority")

    db = conn.desafio_shape

    collection_vessels = db[VESSELS]
    collection_equipments = db[EQUIPMENTS]
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
import os

ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                mongo_db_url = "mongodb+srv://ashishk94412:iRobotplay07@cluster0.v2mggqq.mongodb.net/?retryWrites=true&w=majority"
                #if mongo_db_url is None:
                #   raise Exception(f"Environment Key: {os.getenv(MONGODB_URL_KEY)} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

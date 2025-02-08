# class connect to mongodb and save data

from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId

class MongoDB:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
        self.db = self.client[settings.MONGO_DB]
        self.collection = self.db[settings.MONGO_COLLECTION]

    def insert_one(self, data):
        # insert and return the id of the inserted document
        return self.collection.insert_one(data).inserted_id
    
    # update one key of document with id
    def update_one(self, id, key, value):
        # convert id to ObjectId
        id = ObjectId(id)
        print(id)
        return self.collection.update_one({"_id": id}, {"$set": {key: value}})
    
    # find one document with id
    def find_one(self, id):
        # convert id to ObjectId
        id = ObjectId(id)
        return self.collection.find_one({"_id": id})

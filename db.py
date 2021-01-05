from flask import Flask
import pymongo

CONNECTION_STRING = "mongodb+srv://anb:0000@cluster0.ivu59.mongodb.net/"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')
import datetime
from pymongo import MongoClient


class Observation:
    client = MongoClient(
        'mongodb+srv://mongoCredentials@main.kc4dw.mongodb.net/weather?retryWrites=true&w=majority')
    db = client.get_database('weather')
    records = db.data

    @classmethod
    def upload(cls, temperature, humidity):
        observation = {
            'temperature': temperature,
            'humidity': humidity,
            'time': datetime.datetime.utcnow()
        }
        cls.records.insert_one(observation)

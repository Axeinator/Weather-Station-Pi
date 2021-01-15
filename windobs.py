import datetime
from pymongo import MongoClient
import os

creds = os.getenv("MONGO")

class Observation:
    client = MongoClient(f'mongodb+srv://{creds}@main.kc4dw.mongodb.net/weather?retryWrites=true&w=majority')
    db = client.get_database('weather')
    records = db.wind

    @classmethod
    def upload(cls, temperature, humidity):
        observation = {
            'temperature': temperature,
            'humidity': humidity,
            'time': datetime.datetime.utcnow()
        }
        cls.records.insert_one(observation)

    @classmethod
    def windUpload(cls, speed):
        observation = {
                'speed': speed,
                'time': datetime.datetime.now()
                }
        cls.records.insert_one(observation)

    @classmethod
    def windAvgUpload(cls, speed, gust):
        records = cls.db.windAvg
        observation = {
                'speed': speed,
                'gust': gust,
                'time': datetime.datetime.utcnow()
                }
        records.insert_one(observation)

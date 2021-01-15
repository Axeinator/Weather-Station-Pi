import requests

class Windy:
    key = 'windyAPIKey'
    @classmethod
    def upload(cls, temperature, humidity):
        requests.get(f'http://stations.windy.com/update/{key}/?tempf={temperature}')



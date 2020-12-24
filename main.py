import RPi.GPIO as GPIO
import dht11
from observation import Observation
from windyAPI import Windy
import time
import datetime
import logging
from multiprocessing import Process

def toFaren(temp):
    return (temp * 9/5) + 32

logging.basicConfig(filename='station.log', level=logging.INFO)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor = dht11.DHT11(pin=14)

logging.info(f"Starting weather station: {datetime.datetime.now()}")
def mongoUpload():
    while True:
        try:
            result = sensor.read()
            if result.is_valid():
                Observation.upload(toFaren(result.temperature), result.humidity)
            else:
                logging.warning(f"Invalid result at {datetime.datetime.now()}")
        except:
            logging.error(f"Upload error at {datetime.datetime.now()}")
        time.sleep(120)

def windyUpload():
    while True:
        try:
            result = sensor.read()
            if result.is_valid():
                Windy.upload(toFaren(result.temperature), result.humidity)
            else:
                logging.warning(f'Invalid result at {datetime.datetime.now()}')
        except:
            logging.error(f"Windy Upload error at {datetime.datetime.now()}")
        time.sleep(120)

if __name__ == '__main__':
    mongo = Process(target=mongoUpload)
    windyStation = Process(target=windyUpload)
    mongo.start()
    windyStation.start()
    mongo.join()
    windyStation.join() 
    logging.info(f"Multiprocessing success. Both processes started at {datetime.datetime.now()}")

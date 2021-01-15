import RPi.GPIO as GPIO
import dht11
from observation import Observation
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

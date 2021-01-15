import time
import RPi.GPIO as GPIO
import dht11
from flask import Flask, jsonify

def toFaren(temp):
    return (temp * 9/5) + 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

app = Flask(__name__)

def liveReading():
    sensor = dht11.DHT11(pin=14)
    result = sensor.read()
    while not result.is_valid():
        result = sensor.read()
        time.sleep(3)
    return (toFaren(result.temperature), result.humidity)

@app.route('/')
def live():
    temperature, humidity = liveReading()
    return {'temperature': temperature, 'humidity': humidity}




import RPi.GPIO as GPIO
import dht11
def toFaren(temp):
    return (temp * 9/5) + 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor = dht11.DHT11(pin=14)
result = sensor.read()

print(f'Temperature: {toFaren(result.temperature)}')
print(f'Humidity: {result.humidity}')
print(f'Error Code: {result.error_code}' )

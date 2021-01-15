from gpiozero import Button
import math
import time
import schedule
import statistics
from windobs import Observation

wind_speed_sensor = Button(12)
wind_count = 0
sensorAdjustment = 1.18
interval = 5
speeds = []

def speed(time_sec):
    radius = 9
    circumfrence = (2 * math.pi) * radius   
    rotations = wind_count / 2
    MIdistanceSpun = (circumfrence * rotations) / 160934.4
    speed = (MIdistanceSpun / time_sec) * 3600
    return speed
    

def spin():
    global wind_count
    wind_count += 1

def resetSpin():
    global wind_count
    wind_count = 0

def collect():
    speeds.append(speed(interval))
    resetSpin()
    
def organize():
    global speeds
    gust = max(speeds)
    avg = statistics.mean(speeds)
    try:
        Observation.windAvgUpload(avg, gust)
    except:
        pass
    speeds = []

wind_speed_sensor.when_pressed = spin

schedule.every(5).seconds.do(collect)
schedule.every(120).seconds.do(organize)

while True:
    schedule.run_pending()
    time.sleep(0.5)

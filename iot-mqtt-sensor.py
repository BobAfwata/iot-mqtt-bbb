#!/usr/bin/python

import paho.mqtt.publish as mqtt
import time
import random

# Dummy function to read from a temperature sensor.
def readTemp():
    return random.randint(80,100)

# Deumm function to read from a rain sensor.
def readPrecipitation():
    r = random.randint(0,10)
    if r < 4:
        return 'rain'
    elif r < 8:
        return 'sun'
    else:
        return 'hurricane'
    
while True:
    mqtt.single("iot-mqtt-example/weather/temperature", readTemp(), hostname="test.mosquitto.org")
    mqtt.single("iot-mqtt-example/weather/precipitation", readPrecipitation(), hostname="test.mosquitto.org")
    time.sleep(10)

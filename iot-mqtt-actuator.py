#!/usr/bin/python
import paho.mqtt.client as mqtt

def onConnect(client, obj, flags, rc):
    print("Connected. rc = %s " % rc)
    client.subscribe("iot-mqtt-example/weather/temperature")
    client.subscribe("iot-mqtt-example/weather/precipitation")

# Dummy function to act on temperature data
def temperatureActuator(temperature):
    print("Temperature = %s\n" % temperature)

# Dummy function to act on precipitation data
def precipitationActuator(precipitation):
    action = {
        "rain" : "Grab an umbrella",
        "sun" : "Don't forget the sunscreen",
        "hurricane" : "Buy bread, water and peanut butter."
    }
    print("Precipitation = %s" % precipitation)
    print("\t%s\n" % action[precipitation])
    
def onMessage(mqttc, obj, msg):
    callbacks = {
        "iot-mqtt-example/weather/temperature" : temperatureActuator,
        "iot-mqtt-example/weather/precipitation" : precipitationActuator
    }
    callbacks[msg.topic](msg.payload)

client = mqtt.Client()
client.on_connect = onConnect
client.on_message = onMessage
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()

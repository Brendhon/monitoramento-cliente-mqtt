import paho.mqtt.client as mqtt 
from random import randrange
import time

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Teste")
client.connect(mqttBroker) 

while True:
    randNumber = randrange(10)
    client.publish("c115/test", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
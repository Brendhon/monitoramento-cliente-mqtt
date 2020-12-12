import paho.mqtt.client as mqtt 
from random import randrange, randint
import time
import json

mqttBroker = "test.mosquitto.org" 

client = mqtt.Client("Cliente")
client.connect(mqttBroker) 

idList = [
    "5fd2b042c9671d3d14065858",
    "5fd2b042c9671d3d14065859",
    "5fd2b042c9671d3d1406585a",
    "5fd2b043c9671d3d1406585b",
    "5fd2b043c9671d3d1406585c",
    "5fd2b043c9671d3d1406585d",
    "5fd2b043c9671d3d1406585e",
    "5fd2b043c9671d3d1406585f",
    "5fd2b043c9671d3d14065860",
    "5fd2b043c9671d3d14065861",
    "5fd2b044c9671d3d14065862",
    "5fd2b044c9671d3d14065863"
]

while True:

    # Alterando os valores
    randId = randrange(12)
    randStatus = randint(0, 1)

    obj = {
        '_id': idList[randId],
        'status': randStatus
    }

    # Enviando para o tópico 
    client.publish("c115/projeto/vaga", json.dumps(obj))
    print("Mudança na vaga: " + str(randId + 1)) # Mostrando no console qual vaga foi alterada
    time.sleep(10) # Tempo para alterar
    
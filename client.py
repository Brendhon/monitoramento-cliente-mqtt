import paho.mqtt.client as mqtt 
from random import randrange, randint
import time
import json

mqttBroker = "test.mosquitto.org" 

client = mqtt.Client("Teste")
client.connect(mqttBroker) 

while True:

    # Alterando os valores
    randId = randrange(12)
    randStatus = randint(0, 1)
    randType = randint(1, 3)

    if randType == 1:
        randType = "NORMAL"
    
    if randType == 2:
        randType = "DEFICIENTE"

    if randType == 3:
        randType = "IDOSO"

    obj = {
        'id': randId,
        'status': randStatus,
        'type': randType
    }

    # Enviando para o tópico 
    client.publish("c115/projeto/vaga", json.dumps(obj))
    print("Just published " + str(randId) + " to topic TEMPERATURE") # Mostrando no console
    time.sleep(2) # Tempo para alterar
import paho.mqtt.client as mqtt #import the client1
import time
broker_address="127.0.0.1" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

while True:
    client.publish("toptest","top...")#publish
    time.sleep(10)

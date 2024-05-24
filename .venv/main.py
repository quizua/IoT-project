import sys
from Adafruit_IO import MQTTClient
import time
import random
from uart import *

AIO_FEED_IDs = ["button1","button2"]
AIO_USERNAME = ""
AIO_KEY = ""

def connected(client):
    print("Connected successfully ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed successfully ...")

def disconnected(client):
    print("Disconnected ...")
    sys.exit (1)

def message(client , feed_id , payload): 
    print("Get data " + payload + " , feed id: " + feed_id)
    if feed_id == "button1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "button2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")        
                

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
while True:
    counter-=1
    if counter <= 0:
        counter = 10
        temp = random.randint(25, 35)
        client.publish("sensor1", temp)
        humi = random.randint(50, 70)
        client.publish("sensor2", humi)
    
    # readSerial(client)
    time.sleep(1)
    pass

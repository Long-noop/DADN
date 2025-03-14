import sys
import random
import time
import serial . tools . list_ports
from Adafruit_IO import MQTTClient

AIO_FEED_ID = os.getenv("AIO_FEED_ID")
AIO_USERNAME = os.getenv("AIO_USERNAME")
AIO_KEY = os.getenv("AIO_KEY")

# def connected (client): 
#     print("Ket noi thanh cong...") 
#     client.subscribe (AIO_FEED_ID) 

# def subscribe (client, userdata, mid, granted_qos):
#     print("Subcribe thanh cong...") 

# def disconnected (client): 
#     print("Ngat ket noi...") 
#     sys.exit (1) 

# def message (client, feed_id, payload): 
#     print("Nhan du lieu:" + payload) 

# client = MQTTClient (AIO_USERNAME, AIO_KEY) 
# client.on_connect = connected 
# client.on_disconnect = disconnected 
# client.on_message = message 
# client.on_subscribe = subscribe 
# client.connect() 
# client.loop_background() 
# while True: 
#     pass



def  connected(client):
    print("Ket noi thanh cong...")
    client.subscribe(AIO_FEED_ID)

def  subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong...")

def  disconnected(client):
    print("Ngat ket noi...")
    sys.exit (1)

def  message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    value = random.randint(0, 100)
    print("Cap nhat:", value)
    client.publish("bbc-temp", value)
    time.sleep(30)
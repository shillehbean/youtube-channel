#Native libs
import network
import time

#Third Party
from umqtt.simple import MQTTClient

# Internal libs
import constants


def connectMQTT():
    '''Connects to Broker'''
    # Client ID can be anything
    client = MQTTClient(
        client_id=b"other client",
        server=constants.SERVER_HOSTNAME,
        port=0,
        user=constants.USER,
        password=constants.PASSWORD,
        keepalive=7200,
        ssl=True,
        ssl_params={'server_hostname': constants.SERVER_HOSTNAME}
    )
    client.connect()
    return client


def connect_to_internet(ssid, password):
    # Pass in string arguments for ssid and password
    
    # Just making our internet connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('waiting for connection...')
      time.sleep(1)
    # Handle connection error
    if wlan.status() != 3:
       print(wlan.status())
       raise RuntimeError('network connection failed')
    else:
      print('connected')
      print(wlan.status())
      status = wlan.ifconfig()

def make_connections():
    # Connect to internet and set MPU to start taking readings
    connect_to_internet(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)
    return connectMQTT()


def my_callback(topic, response):
    # Perform desired actions based on the subscribed topic and response
    print("Received message on topic:", topic)
    print("Response:", response)


def subscribe(topic, client):
    '''Recieves data from the broker'''
    client.subscribe(topic)
    print("Subscribe Done")

client = make_connections()
client.set_callback(my_callback)
subscribe('Topic', client)

while True:
   time.sleep(5)
   client.check_msg()
    

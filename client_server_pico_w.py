# server

from machine import Pin, ADC
import network
import random
import socket
import time

import constants


# Just making our internet connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)

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
   raise RuntimeError('network connection failed')
else:
  print('connected')
  status = wlan.ifconfig()
  #print('ip = ' + status[0])

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        request = cl.recv(1024)
        print(request)
        # No need to unpack request in this example
        ran_num = str(random.randint(0, 100))
        cl.send(ran_num)
        print("Sent: " + ran_num)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')

####################
#client code

# Program to read RGB values from a local Pico Web Server
# Tony Goodhew 5th July 2022
# Connect to network
from machine import Pin, ADC
import network
import random
import socket
import time

import constants

# Just making our internet connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)

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
   raise RuntimeError('network connection failed')
else:
  print('connected')
  status = wlan.ifconfig()
  #print('ip = ' + status[0])

while True:
    ai = socket.getaddrinfo("192.168.1.92", 80) # Address of Web Server
    addr = ai[0][-1]

    # Create a socket and make a HTTP request
    s = socket.socket() # Open socket
    s.connect(addr)
    s.send(b"Anything") # Send request
    ss=str(s.recv(512)) # Store reply
    # Print what we received
    print(ss)
    # Set RGB LED here
    s.close()          # Close socket
    time.sleep(0.2)    # wait


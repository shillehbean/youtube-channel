import time
import network

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
       raise RuntimeError('network connection failed')
    else:
      print('connected')
      status = wlan.ifconfig()
      
connect_to_internet('<your internet name>', '<your internet password>')

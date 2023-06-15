from machine import Pin, I2C
import network
import time

from blynklib import Blynk
import bme280

import constants


i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
BLYNK = Blynk(constants.BLYNK_AUTH_TOKEN)


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


connect_to_internet(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)


while True:
    bme = bme280.BME280(i2c=i2c)
    temperature, pressure, humidity = bme.read_compensated_data()
    # Print sensor data to console
    print('Temperature: {:.1f} C'.format(temperature/100))
    print('Humidity: {:.1f} %'.format(humidity/1024))
    print('Pressure: {:.1f} hPa'.format(pressure/25600))
    BLYNK.virtual_write(7, temperature/100)
    BLYNK.virtual_write(8, humidity/1024)
    BLYNK.virtual_write(9, pressure/25600)
    BLYNK.run()
    time.sleep(1)

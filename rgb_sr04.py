from machine import Pin, time_pulse_us
import time
from neopixel import Neopixel

numpix = 6
pixels = Neopixel(numpix, 0, 28)
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color0 = red

 
while True:
    if color0 == red:
       color0 = blue
       color1 = blue
    else:
        color0 = blue
        color1 = blue
    pixels.set_pixel(0, color0)
    pixels.set_pixel(1, color0)
    pixels.set_pixel(2, color0)
    pixels.set_pixel(3, yellow)
    pixels.set_pixel(4, blue)
    pixels.set_pixel(5, red)
    pixels.show()
    time.sleep(1)

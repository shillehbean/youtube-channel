from machine import Pin, time_pulse_us
import random
import time


from neopixel import Neopixel


# You can change the pins you use
SOUND_SPEED=340
TRIG_PULSE_DURATION_US=10
TRIG_PIN = Pin(15, Pin.OUT)
ECHO_PIN = Pin(14, Pin.IN)
# Set params for Neopixel
NUMPIX = 6
PIXELS = Neopixel(NUMPIX, 0, 28)
YELLOW = (255, 100, 0)
ORANGE = (255, 50, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LAVENDER = (230, 230, 250)
# You can add as many colors as you want
COLOR_DICT = {0: YELLOW, 1: ORANGE, 2: GREEN, 3: BLUE, 4: RED, 5: LAVENDER}


def get_distance():
    '''Returns distance in CM'''
    TRIG_PIN.value(0)
    time.sleep_us(5)
    TRIG_PIN.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    TRIG_PIN.value(0)
    ultrason_duration = time_pulse_us(ECHO_PIN, 1, 30000)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    print(f"Distance : {distance_cm} cm")
    return distance_cm


def change_color_with_distance():
    '''Can be used to change color depending on distance'''
    while True:
        distance = get_distance()
        if distance < 10:
            color = RED
        elif distance < 20:
            color = YELLOW
        else:
            color = GREEN
        # I set all 6 LEDs to the same value
        # Note that they can all be toggled individually
        for i in range(NUMPIX):
            PIXELS.set_pixel(i, color)
        PIXELS.show()
        time.sleep(1)

    return


def fun():
    '''Loops through random colors you assigned in the constants
       You can also play with the brightness, see neopixel.py code
       for more details ;)'''

    while True:
        # we select a random led, we have a total of 6 (0-5)
        random_led = random.randint(0, 5)
        # we get a random color from the dictionary and assign it to
        # that random LED
        random_color = random.randint(0, len(COLOR_DICT) - 1)
        print(random_led, COLOR_DICT[random_color])
        PIXELS.set_pixel(random_led, COLOR_DICT[random_color])
        PIXELS.show()
        time.sleep(0.5)

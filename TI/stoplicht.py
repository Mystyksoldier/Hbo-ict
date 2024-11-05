import time
from machine import Pin
import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

greenButton = Pin(0, Pin.IN, pull=Pin.PULL_DOWN)
redButton = Pin(1, Pin.IN, pull=Pin.PULL_DOWN)
orangeButton = Pin(2, Pin.IN, pull=Pin.PULL_DOWN)

def greenToRed():
    np[7] = (0, 100, 0)
    np.write()
    time.sleep(3)
    np[7] = (0, 0, 0)
    np[6] = (255, 165, 0)
    np.write()
    time.sleep(1.5)
    np[6] = (0, 0, 0)
    np[5] = (255, 0, 0)
    np.write()
    time.sleep(3)
    np[5] = (0, 0, 0)
    np.write()

def redToGreen():
    np[5] = (255, 0, 0)
    np.write()
    time.sleep(3)
    np[5] = (0, 0, 0)
    np[6] = (255, 165, 0)
    np.write()
    time.sleep(1.5)
    np[6] = (0, 0, 0)
    np[7] = (0, 100, 0)
    np.write()
    time.sleep(3)
    np[7] = (0, 0, 0)
    np.write()

def Orange():
    np[6] = (255, 165, 0)
    np.write()
    time.sleep(1)
    np[6] = (0, 0, 0)
    np.write()
    time.sleep(1)
    np[6] = (255, 165, 0)
    np.write()
    time.sleep(1)
    np[6] = (0, 0, 0)
    np.write()
    time.sleep(1)
    np[6] = (255, 165, 0)
    np.write()
    time.sleep(1)
    np[6] = (0, 0, 0)
    np.write()
    time.sleep(1)

while True:
    if greenButton.value():
        print("Green Button Pressed")
        greenToRed()
    if redButton.value():
        print("Red Button Pressed")
        redToGreen()
    if orangeButton.value():
        print("Orange Button Pressed")
        Orange()






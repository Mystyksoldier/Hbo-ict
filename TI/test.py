import time
from machine import Pin
import machine
import neopixel

np1 = neopixel.NeoPixel(machine.Pin(2), 30)

ledcollor = (255, 0, 0)

def LedDemo():
    for i in range(30):
        if i != 0:
            np1[i - 1] = (255, 0, 255)
            np1.write()
        np1[i] = ledcollor
        np1.write()
        time.sleep(0.1)
    for i in range(29, -1, -1):
        np1[i] = (0, 0, 0)
        np1.write()
        time.sleep(0.1)


while True:
    LedDemo()
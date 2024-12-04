import time
from machine import Pin
import machine
import neopixel

np1 = neopixel.NeoPixel(machine.Pin(0), 8)
np2 = neopixel.NeoPixel(machine.Pin(0), 8)
np3 = neopixel.NeoPixel(machine.Pin(0), 8)

def LedDemo():
    for i in range(8):
        if i != 0:
            np1[i - 1] = (255, 0, 255)
            np1.write()
        np1[i] = (255, 0, 0)
        np1.write()
        time.sleep(0.5)
    for i in range(7, -1, -1):
        np1[i] = (0, 0, 0)
        np1.write()
        time.sleep(0.5)


while True:
    LedDemo()
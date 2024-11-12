# 1*1 + 1*2 + 0*4 + 1*8 + 0*16 + 1*32 + 0*64 + 1*128 = 171

from machine import Pin
import time

pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]

def frontToBack():
    for i, pin in enumerate(pins):
        pin.value(1)
        time.sleep(0.5)
        pin.value(0)
        time.sleep(0.5)

def backToFront():
    for i, pin in reversed(list(enumerate(pins))):
        pins[i].value(1)
        time.sleep(0.5)
        pins[i].value(0)
        time.sleep(0.5)

while True:
    frontToBack()
    backToFront()
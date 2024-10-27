from machine import Pin
import time

led_pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]
switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if switch_pin.value():
        for led in led_pins:
            led.value(1)
    
    if switch_pin.value():
        for led in led_pins:
            led.value(0)
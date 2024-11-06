from machine import Pin
import time

led_pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT)]
switch_pin_on = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
switch_pin_off = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if switch_pin_on.value():
        for led in led_pins:
            led.value(1)
    
    if switch_pin_off.value():
        for led in led_pins:
            led.value(0)

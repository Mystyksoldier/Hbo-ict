from machine import Pin
import time

led_pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]

while True:
    # Turn on all LEDs
    for led in led_pins:
        led.value(1)
    time.sleep(0.5)

    # Turn off all LEDs
    for led in led_pins:
        led.value(0)
    time.sleep(0.5)

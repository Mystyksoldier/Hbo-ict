from machine import Pin
import time

led_pins = Pin(20, Pin.OUT)

while True:
    led_pins.value(1)
    time.sleep(0.5)
    led_pins.value(0)
    time.sleep(0.5)

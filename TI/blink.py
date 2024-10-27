import machine
import time
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()  # Toggle the LED state
    time.sleep(1)  # Wait for 1 second


from machine import Pin
import machine
import time
import neopixel

np = neopixel.NeoPixel(machine.Pin(3), 30)

trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

SPEED_OF_SOUND = 343

def measure_distance():
    # Send a 10 microsecond pulse to trigger the sensor
    trigger_pin.value(0)
    time.sleep_us(2)
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)
    
    
    # Wait for the echo_pin and measure the time
    while echo_pin.value() == 0:
        start_time = time.ticks_us()
    
    while echo_pin.value() == 1:
        end_time = time.ticks_us()
    
    # Calculate elapsed time in microseconds
    elapsed_time = time.ticks_diff(end_time, start_time)
    
    # Calculate the distance
    distance = (SPEED_OF_SOUND * elapsed_time) / (2 * 1_000_000)
    return distance

def blink_led():
    if measure_distance() < 0.15:
        print("Distance is less than 10 cm")
        for i in range(30):
            np[i] = (255, 0, 0)
            np.write()
            time.sleep(0.1)

        time.sleep(1)

        for i in range(29, -1, -1):
            np[i] = (0, 0, 0)
            np.write()
            time.sleep(0.1)
    else:
        print("Distance is more than 10 cm")
        for i in range(30):
            np[i] = (0, 0, 0)
            np.write()
while True:
        
    blink_led()
    time.sleep(0.1)
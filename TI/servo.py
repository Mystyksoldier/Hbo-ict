from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(0))
redButton = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
greenButton = Pin(14, Pin.IN, pull=Pin.PULL_DOWN)
pwm.freq(100)

while True:
    if redButton.value() == 1:
        for duty in range(6553, 13107, 50):
            pwm.duty_u16(duty)
            sleep(0.01)
    if greenButton.value() == 1:
        for duty in range(13107, 6553, -50):
            pwm.duty_u16(duty)
            sleep(0.01)
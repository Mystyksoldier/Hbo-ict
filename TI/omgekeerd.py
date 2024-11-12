from machine import ADC, PWM, Pin
import time

led = PWM(Pin(20))
led.freq(1000)

adc = ADC(Pin(26))


def pulse(interval):
    led.duty_u16(65535)
    time.sleep(interval / 2)
    led.duty_u16(0)
    time.sleep(interval / 2)

while True:

    adc_value = adc.read_u16()
    interval = 0.1 + (adc_value / 65535) * 0.9

    pulse(interval)
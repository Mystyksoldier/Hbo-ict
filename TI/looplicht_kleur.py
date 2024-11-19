from machine import Pin , ADC
import machine
import neopixel
import time

np = neopixel.NeoPixel(machine.Pin(0), 8)

adc = ADC(4)


def ReadTemperature():
	adc_value = adc.read_u16()
	volt = (3.3/65535) * adc_value
	temperature = 27 - (volt - 0.706)/0.001721
	return round(temperature, 1)

def LedDemo():
    for i in range(8):
        np[i] = (255, 0, 0)
        np.write()
        time.sleep(0.5)
        
    for i in range(8):
        np[i] = (0, 0, 255)
        np.write()

    time.sleep(1)

    for i in range(8):
        np[i] = (0, 102, 0)
        np.write()
    time.sleep(1)


while True:
    LedDemo()
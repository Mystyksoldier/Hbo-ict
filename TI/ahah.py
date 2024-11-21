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
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(0.1)
    np[1] = (255, 0, 0)
    np[0] = (0, 102, 0)
    np.write()
    time.sleep(0.1)
    np[2] = (255, 0, 0)
    np[1] = (0, 102, 0)
    time.sleep(0.1)
    np[3] = (255, 0, 0)
    np[2] = (0, 102, 0)
    np.write()
    time.sleep(0.1)
    np[0] = (0, 255, 0)
    np[4] = (255, 0, 0)
    np[3] = (0, 102, 0)
    time.sleep(0.1)
    np[5] = (255, 0, 0)
    np[4] = (0, 102, 0)
    np.write()
    time.sleep(0.1)
    np[6] = (255, 0, 0)
    np[5] = (0, 102, 0)
    time.sleep(0.1)
    np[7] = (255, 0, 0)
    np[6] = (0, 102, 0)
    np.write()
    time.sleep(0.1)
    np[7] = (0, 102, 0)



while True:
    LedDemo()
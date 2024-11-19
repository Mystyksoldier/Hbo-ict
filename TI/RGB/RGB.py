from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import time
import neopixel
"""
From the 1602A LCD Datasheet. The I2C 1602 LCD module is a 2 line by 16 character display interfaced to an I2C daughter board.
Specifications: 2 lines by 16 characters
I2C Address Range: 0x20 to 0x27 (Default=0x27, addressable) 
Operating Voltage: 5 Vdc 
Contrast: Adjustable by potentiometer on I2C interface
Size: 80mm x 36mm x 20 mm
Viewable area: 66mm x 16mm 

Drivers provided by https://www.circuitschools.com/
Note: Adjust the potentiometer when you do not see any characters on the display 
"""

time.sleep(0.5)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

redButton = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
greenButton = Pin(14, Pin.IN, pull=Pin.PULL_DOWN)
np = neopixel.NeoPixel(machine.Pin(13), 8)


def redLed():
    for i in range(7):
        np[i] = (255, 0, 0)
        np.write()
        time.sleep(0.2)
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.5)

    for i in range(4):
        np[7] = (255, 0, 0)
        np.write()
        time.sleep(0.2)
        np[7] = (0, 0, 0)
        np.write()
        time.sleep(0.2)

def greenLed():
    for i in range(7):
        np[i] = (0, 100, 0)
        np.write()
        time.sleep(0.2)
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.5)

    for i in range(4):
        np[7] = (0, 100, 0)
        np.write()
        time.sleep(0.2)
        np[7] = (0, 0, 0)
        np.write()
        time.sleep(0.2)

def red():
    lcd.move_to(3, 0)
    lcd.putstr("Red Button")
    lcd.move_to(4, 1)
    lcd.putstr("Pressed")
    redLed()
    time.sleep(1.5)
    lcd.clear()

def green():
    lcd.move_to(2, 0)
    lcd.putstr("Green Button")
    lcd.move_to(4, 1)
    lcd.putstr("Pressed")
    greenLed()
    time.sleep(1.5)
    lcd.clear()

while True:
    if redButton.value() == 1:
        red()
    if greenButton.value() == 1:
        green()


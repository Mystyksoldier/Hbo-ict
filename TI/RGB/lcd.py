from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import time

time.sleep(0.5)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

redButton = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
greenButton = Pin(14, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if redButton.value() == 1:
        lcd.move_to(3, 0)
        lcd.putstr("Red Button")

    if greenButton.value() == 1:
        lcd.move_to(3, 0)
        lcd.putstr("Green Button")


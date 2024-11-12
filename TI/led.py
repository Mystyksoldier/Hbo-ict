from machine import I2C, Pin
from mp_i2c_lcd1602 import LCD1602
from time import sleep_ms

i2c = I2C(1, sda=Pin(0), scl=Pin(1))

LCD = LCD1602(i2c)

LCD.puts("I2C LCD1602")
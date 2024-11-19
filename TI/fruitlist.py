from machine import ADC, PWM, Pin, I2C
from pico_i2c_lcd import I2cLcd
import time

acd = ADC(Pin(26))

fruits = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", 
    "Honeydew", "Indian Fig", "Jackfruit", "Kiwi", "Lemon", "Mango", 
    "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tangerine"
]

time.sleep(0.5)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


acd_value = acd.read_u16()

def CalculateACDPResentage():
    acd_value = acd.read_u16()
    return (acd_value / 65535) * 20



def Show():
    x = enumerate(fruits)
    for i in x:
        if i[0] == CalculateACDPResentage():
            return i[1]


while True:
    print(Show())
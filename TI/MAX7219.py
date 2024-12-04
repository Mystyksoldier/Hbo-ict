import max7219
from machine import Pin, SPI
from time import sleep

# SPI configuration
spi = SPI(1, baudrate=10000000, polarity=0, phase=0)  # SPI channel 1
cs = Pin(1, Pin.OUT)  # Chip select

# Initialize MAX7219 with an 8x8 LED matrix
display = max7219.Matrix8x8(spi, cs, 1)  # '1' for one cascaded module
display.brightness(5)  # Set brightness level (0 to 15)
display.fill(0)  # Clear the display
display.show()

# Display a character
display.text("Q", 0, 0, 1)  # Text, x, y, brightness
display.show()
sleep(2)

# Scrolling text
display.fill(0)
for i in range(10):
    display.scroll(-1, 0)  # Scroll left by 1 pixel
    display.show()
    sleep(0.1)

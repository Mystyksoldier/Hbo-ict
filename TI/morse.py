from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """

    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


def morse(pin, dot_length, text):
    """
    Laat de text horen als morse code.
    De pin is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: spatie, streepje, punt.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """

    for char in text:
        if char == '.':
            pulse(pin, dot_length, dot_length)
        elif char == '-':
            pulse(pin, 3 * dot_length, dot_length)
        elif char == ' ':
            time.sleep(7 * dot_length)
        time.sleep(3 * dot_length)

morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")
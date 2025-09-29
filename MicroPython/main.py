"""
Created by: Alexander
Created on: Sep 2025
This module turns on and off a LED.
"""

from microbit import *

display.clear()
display.show(Image.HAPPY)


while True:
    if button_a.is_pressed():
        # turns on pin 16
        display.show(Image.YES)
        pins.digital_write_pin(DigitalPin.P16, 1)

while True:
    if button_b.is_pressed():
        # turns off pin 16
        display.show(Image.NO)
        pins.digital_write_pin(DigitalPin.P16, 0)

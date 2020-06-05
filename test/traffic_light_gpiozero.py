#from gpiozero.pins.rpigpio import RPiGPIOPin
from gpiozero import LED
from time import sleep

ledred = LED(16)
ledorange = LED(20)
ledgreen = LED(21)

while True:
    ledred.on()
    sleep(4)
    ledorange.on()
    sleep(1)
    ledred.off()
    ledorange.off()
    ledgreen.on()
    sleep(3)
    for x in range(1,4):
        ledgreen.off()
        sleep(0.8)
        ledgreen.on()
        sleep(0.8)
    ledgreen.off()
    ledorange.on()
    sleep(2)
    ledorange.off()


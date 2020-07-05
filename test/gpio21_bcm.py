#!/usr/bin/python3
import RPi.GPIO as GPIO
import time


led = 21
stime = 0.5

GPIO.setmode(GPIO.BCM)

print("GPIO.setup led ")
GPIO.setup(led, GPIO.OUT)


while True:
    GPIO.output(led, True)
    print('led on ')
    time.sleep(stime)
    GPIO.output(led, False)
    print('led off ')
    time.sleep(stime)


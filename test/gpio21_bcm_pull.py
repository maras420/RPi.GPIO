#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os


led = 21
stime = 2

os.environ['RPIGPIO_DEBUG'] = "2"
print("Debug level set to " + os.environ["RPIGPIO_DEBUG"])

GPIO.setmode(GPIO.BCM)

print("GPIO.setup led ")
GPIO.setup(led, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('led on')

while True:
    if GPIO.input(led):
      GPIO.setup(led, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      print('led off')
    else:
      GPIO.setup(led, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      print('led on')
    time.sleep(stime)


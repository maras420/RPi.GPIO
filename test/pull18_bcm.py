#!/usr/bin/python3
import RPi.GPIO as GPIO
import time


led = 18
stime = 2

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


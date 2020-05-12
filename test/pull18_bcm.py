#!/usr/bin/python3
import RPi.GPIO as GPIO
import time


led = 18
stime = 0.5

GPIO.setmode(GPIO.BCM)

print("GPIO.setup led ")
GPIO.setup(led, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(led):
      print('led on')
      GPIO.setup(led, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    else:
      print('led off')
      GPIO.setup(led, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    time.sleep(stime)


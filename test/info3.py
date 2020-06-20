#!/usr/bin/python3
import RPi.GPIO as GPIO

print("RPi.GPIO version: %s\n" % GPIO.VERSION);
print("Pi Board Information")
print("--------------------")
for key,val in GPIO.RPI_INFO.items():
    print("%s => %s" %(key,val));

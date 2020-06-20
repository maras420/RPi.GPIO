from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=27, trigger=17, max_distance=1, threshold_distance=0.3)
while True:
  print('Distance ',sensor.distance, ' m')
  sleep(2)


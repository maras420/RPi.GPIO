from gpiozero import Button
from signal import pause
import os

def ButtonPushed():
    print("Button pushed")

os.environ['RPIGPIO_DEBUG'] = "4"
print("Debug level set to " + os.environ["RPIGPIO_DEBUG"])

button = Button(26,pull_up=False,bounce_time=0.2)
#button = Button(26,pull_up=False)
button.when_pressed = ButtonPushed

pause()


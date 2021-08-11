import RPi.GPIO as GPIO
from time import *
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
 
while True:
    GPIO.output(21, GPIO.HIGH)
    sleep(1)
    GPIO.output(21, GPIO.LOW)
    sleep(1)

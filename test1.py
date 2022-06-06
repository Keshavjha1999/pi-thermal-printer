import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(8, GPIO.HIGH)
    GPIO.setup(10, GPIO.HIGH)
    time.sleep(5)
    GPIO.setup(8, GPIO.LOW)
    GPIO.setup(10, GPIO.LOW)
    time.sleep(5)
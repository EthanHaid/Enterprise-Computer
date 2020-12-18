import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

outPin = 17
inPin = 27

GPIO.setup(outPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  GPIO.output(outPin, GPIO.HIGH)
  print(GPIO.input(inPin) == GPIO.HIGH)
  
  GPIO.output(outPin, GPIO.LOW)
  print(GPIO.input(inPin) == GPIO.HIGH)
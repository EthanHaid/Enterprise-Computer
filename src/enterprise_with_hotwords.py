import RPi.GPIO as GPIO
from time import sleep
from snowboy import detect_hotwords

redPin = 18
greenPin = 13
bluePin = 27
inPin = 17

currentState = (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(greenPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bluePin, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def setLEDs(r = GPIO.HIGH, g = GPIO.HIGH, b = GPIO.HIGH):
  GPIO.output(redPin, r)
  GPIO.output(greenPin, g)
  GPIO.output(bluePin, b)
  currentState = (r, g, b)

def firePhasers():
  print("Fire Phasers!")
  (r, g, b) = currentState

  setLEDs(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
  sleep(0.15)
  setLEDs(GPIO.LOW, GPIO.LOW, GPIO.LOW)
  sleep(0.15)
  setLEDs(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
  sleep(0.15)
  setLEDs(GPIO.LOW, GPIO.LOW, GPIO.LOW)
  sleep(0.5)

  setLEDs(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
  sleep(0.15)
  setLEDs(GPIO.LOW, GPIO.LOW, GPIO.LOW)
  sleep(0.15)
  setLEDs(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
  sleep(0.15)

  setLEDs(r, g, b)

def powerOff():
  print("Power Off!")
  setLEDs(GPIO.LOW, GPIO.LOW, GPIO.LOW)

def powerOn():
  print("Power On!")
  setLEDs(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)

def redAlert():
  print("Red Alert!")
  setLEDs(GPIO.HIGH, GPIO.LOW, GPIO.LOW)

def shieldsUp():
  print("Shields Up!")
  setLEDs(GPIO.LOW, GPIO.LOW, GPIO.HIGH)

def standDown():
  print("Stand Down!")
  setLEDs(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)

def yellowAlert():
  print("Yellow Alert!")
  setLEDs(GPIO.HIGH, GPIO.HIGH, GPIO.LOW)

models = ['models/Enterprise_ Fire phasers!.pmdl',
          'models/Enterprise_ Power Off!.pmdl',
          'models/Enterprise_ Power On!.pmdl',
          'models/Enterprise_ Red alert!.pmdl',
          'models/Enterprise_ Shields up!.pmdl',
          'models/Enterprise_ Stand Down!.pmdl',
          'models/Enterprise_ Yellow alert!.pmdl']

callbacks = [lambda: firePhasers(),
             lambda: powerOff(),
             lambda: powerOn(),
             lambda: redAlert(),
             lambda: shieldsUp(),
             lambda: standDown(),
             lambda: yellowAlert()]

detect_hotwords.detect(models, callbacks)

setLEDs(GPIO.LOW, GPIO.LOW, GPIO.LOW)
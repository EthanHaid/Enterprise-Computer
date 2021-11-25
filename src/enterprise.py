import RPi.GPIO as GPIO
from timeit import default_timer as timer
from time import sleep
import threading
from ir import get_IR_command 

# time, GPIO pin, state
timings = [
  [ 0.130, 1, GPIO.HIGH],
  [ 0.267, 2, GPIO.HIGH],
  [ 0.404, 3, GPIO.HIGH],
  [ 0.470, 22, GPIO.HIGH],
  [ 0.541, 4, GPIO.HIGH],
  [ 0.678, 5, GPIO.HIGH],
  [ 0.815, 6, GPIO.HIGH],
  [ 0.952, 7, GPIO.HIGH],
  [ 1.089, 8, GPIO.HIGH],
  [ 1.226, 9, GPIO.HIGH],
  [ 1.363, 10, GPIO.HIGH],
  [ 1.430, 23, GPIO.HIGH],
  [ 1.500, 11, GPIO.HIGH],
  [ 1.637, 12, GPIO.HIGH],
  [ 1.774, 13, GPIO.HIGH],
  [ 1.911, 14, GPIO.HIGH],
  [ 2.048, 15, GPIO.HIGH],
  [ 2.185, 16, GPIO.HIGH],
  [ 2.322, 17, GPIO.HIGH],
  [ 2.389, 22, GPIO.HIGH],
  [ 2.459, 18, GPIO.HIGH],
  [ 2.596, 19, GPIO.HIGH],
  [ 2.733, 20, GPIO.HIGH],
  [ 2.870, 21, GPIO.HIGH],
  [ 3.349, 23, GPIO.HIGH],
  [ 4.308, 22, GPIO.HIGH],
  [ 5.268, 23, GPIO.HIGH],
  [ 6.227, 22, GPIO.HIGH],
  [ 7.187, 23, GPIO.HIGH],
  [ 8.146, 22, GPIO.HIGH],
  [ 9.106, 23, GPIO.HIGH],
  [ 10.065, 22, GPIO.HIGH],
  [ 11.025, 23, GPIO.HIGH],
  [ 11.984, 22, GPIO.HIGH],
  [ 12.944, 23, GPIO.HIGH],
  [ 13.903, 23, GPIO.LOW],
  [ 14.600, 21, GPIO.LOW],
  [ 14.737, 20, GPIO.LOW],
  [ 14.874, 19, GPIO.LOW],
  [ 15.011, 18, GPIO.LOW],
  [ 15.148, 17, GPIO.LOW],
  [ 15.285, 16, GPIO.LOW],
  [ 15.422, 15, GPIO.LOW],
  [ 15.559, 14, GPIO.LOW],
  [ 15.696, 13, GPIO.LOW],
  [ 15.833, 12, GPIO.LOW],
  [ 15.970, 11, GPIO.LOW],
  [ 16.107, 10, GPIO.LOW],
  [ 16.244, 9, GPIO.LOW],
  [ 16.381, 8, GPIO.LOW],
  [ 16.518, 7, GPIO.LOW],
  [ 16.655, 6, GPIO.LOW],
  [ 16.792, 5, GPIO.LOW],
  [ 16.929, 4, GPIO.LOW],
  [ 17.066, 3, GPIO.LOW],
  [ 17.203, 2, GPIO.LOW],
  [ 17.340, 1, GPIO.LOW],
]

# Initialize pins 
# 0-23: output low - Shields & Red Alert
# 24: output high - Ready!
def init():
  print("Initializing...")
  GPIO.setmode(GPIO.BCM)

  for i in range(24):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

  GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
  print("Done")

# Chase shield lights
def bootAnimation():
  print("Boot Animation...")

  for i in range(2):
    for j in range(21):
      GPIO.output(j+1, GPIO.HIGH)
      sleep(0.1)
      GPIO.output(j+1, GPIO.LOW)
      
  print("Done")

# Set pins 1-21 to a given state
def setShields(state):
  for i in range(1, 22):
    GPIO.output(i, state)

# Set shields to high
def raiseShields():
  print("Shields High...")
  setShields(GPIO.HIGH)
  print("Done")

# Set shields to low
def lowerShields():
  print("Shields Low...")
  setShields(GPIO.LOW)
  print("Done")

# Play shield animation
def animateShields():
  print("Play Animation...")

  start = timer()
  i = 0
  timing = timings[0]

  while True:
    end = timer()
    if end - start > timing[0]:
      GPIO.output(timing[1], timing[2])

      # Red alert pins
      if timing[1] == 22: 
        GPIO.output(23, GPIO.LOW)
      elif timing[1] == 23: 
        GPIO.output(22, GPIO.LOW)

      i += 1
      if i >= len(timings):
        break
      timing = timings[i]

  print("Done")


ir_mappings = {
  "BUTTON_1": animateShields,
  "BUTTON_2": animateShields,
  "BUTTON_3": animateShields,
  "BUTTON_4": animateShields,
  "BUTTON_5": animateShields,
}
  
if __name__ == "__main__":
  init()
  bootAnimation()
  lowerShields()

  # Event loop
  try:
    while True:
      command = get_IR_command()
      if command:
        print(command)
        thread = threading.Thread(target = ir_mappings[command])
        thread.start()

  except KeyboardInterrupt:
    GPIO.cleanup()

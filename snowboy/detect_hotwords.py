import snowboydecoder
import sys
import signal

# Listening for Enterprise hotwords

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def goprint(str):
    print(str)

if len(sys.argv) != 5:
    print("Error: need to specify 4 model names")
    print("Usage: python detect_hotwords.py models/*")
    sys.exit(-1)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: goprint("Fire phasers!"),
             lambda: goprint("Red alert!"),
             lambda: goprint("Shields up!"),
             lambda: goprint("Yellow alert!")]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

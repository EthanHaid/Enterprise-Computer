import snowboydecoder
import sys
import signal

# Listening for hotwords

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def detect(models, callbacks):
    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    sensitivity = [0.5]*len(models)
    detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    # make sure you have the same numbers of callbacks and models
    detector.start(detected_callback=callbacks,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)

    detector.terminate()

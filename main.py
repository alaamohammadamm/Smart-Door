import cv2
import time
import numpy as np
from model import Model
from picamera2 import Picamera2
from stepper import Stepper
import RPi.GPIO as GPIO


Stepper = Stepper()

model = Model()
# Temporary vaiables for names:
authorized = "brown"
unauthorized = "white"
background = "none"

exposure = 10000
gain = 2.0




cam = Picamera2()
cam.framerate = 100
cam.configure(cam.create_preview_configuration(main={"format" : "BGR888"}))
cam.start()
cam.set_controls({"ExposureTime": exposure, "AnalogueGain": gain})
time.sleep(2)


while True:
    frame = cam.capture_array()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Camera Feed", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cv2.waitKey(50)
    result = model.assess(frame)


    if (result == authorized):
        Stepper.open_close_door()
        print("ENABLED")

GPIO.cleanup()

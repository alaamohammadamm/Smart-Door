import RPi.GPIO as GPIO
import time


class Stepper:

    # GPIO pin definitions.
    DIR = 20  # DIRECTION
    STEP = 21  # STEP
    SLEEP = 19  # SLEEP
    MODE = (5, 6, 13) #Microstepping resolution
    

    # Constant Values.
    MICROSTEPPING = 16.0  # Microstepping number used for variable calculation.
    CW = 1  # Clockwise
    CCW = 0  # Counter-Clockwise
    SD = 0.004 / MICROSTEPPING # Delay between steps in seconds.
    OPEN = int(650 * (MICROSTEPPING))  # Steps to open and close door.
    OPEN_DURATION = 3  # Seconds door stays open.
    # Microstepping resolution
    RESOLUTION = {'Full': (0, 0, 0), 
                  'Half':  (1, 0, 0), 
                  '1/4': (0, 1, 0),
                  '1/8': (1, 1, 0),
                  '1/16': (0, 0, 1),
                  '1/32': (1, 0, 1)}


    def __init__(self):

        # Initialize pins. 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.SLEEP, GPIO.OUT)
        GPIO.setup(self.MODE, GPIO.OUT)
        GPIO.output(self.MODE, self.RESOLUTION['1/16'])

    def step(self, step_count):

        GPIO.output(self.SLEEP, GPIO.HIGH)  # Wakes up the motor.
        time.sleep(0.1) # Small delay


        # Steps the stepper motor #step_count times. 
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.SD)
            GPIO.output(self.STEP, GPIO.LOW)
            print(f"Step {x}.")

    def open_close_door(self):

        GPIO.output(self.DIR, self.CCW)  # Sets the motor direction
        time.sleep(0.1) # Small delay

        self.step(self.OPEN) # Opens door.
        time.sleep(self.OPEN_DURATION)  # Duration it stays open.
        print("Door has opened.")

        GPIO.output(self.DIR, self.CW)  # Reverses direction.
        time.sleep(0.1) # Small delay

        self.step(self.OPEN)
        print("Door has closed")

        GPIO.output(self.SLEEP, GPIO.LOW)  # Sleeps the motor (No longer applies torque and shuts noise)

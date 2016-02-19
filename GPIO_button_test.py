# Test the buttons in three ways:
# mode1() for basic continuous input; tests that buttons 1 .. 4 are all working as they should.
# mode2() tests for push button combinational input
# mode3() tests for switch on/off combinational input

import RPi.GPIO  as GPIO
import time

def mode1():
    GPIO.setmode(GPIO.BOARD)
    but_1 = 16                            
    GPIO.setup(but_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    try:
        while True:
            if (GPIO.input(but_1) == 1):
                print "BUTTON 1"
                time.sleep(0.2)
            else:
                print "OFF"
                time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()

mode1()

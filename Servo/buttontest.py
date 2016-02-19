import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


but_ser = 16 #pin of the button for the servo routine


GPIO.setup(but_ser, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


option =  True
while (option):
    if (GPIO.input(but_ser) == 1):
        print "Hello"

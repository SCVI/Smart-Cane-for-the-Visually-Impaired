import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 12
PWMpin = 7

GPIO.setup(PWMpin, GPIO.OUT)
p = GPIO.PWM(PWMpin,207)

p.start(0)
timeout = 0.020

while 1:
        GPIO.setup(TRIG, GPIO.OUT)
        #cleanup output
        GPIO.output(TRIG, 0)
        time.sleep(0.000002)

        #send signal
        GPIO.output(TRIG, 1)
        time.sleep(0.000005)
        GPIO.output(TRIG, 0)
        GPIO.setup(ECHO, GPIO.IN)
        
        goodread=True
        watchtime=time.time()
        while (GPIO.input(ECHO)== 0 and goodread):
                starttime=time.time()
                if (starttime-watchtime > timeout):
                        goodread=False

        if goodread:
                watchtime=time.time()
                while (GPIO.input(ECHO)== 1 and goodread):
                        endtime=time.time()
                        if (endtime-watchtime > timeout):
                                goodread=False
        
        if goodread:
                duration=endtime-starttime
                distance=duration*34000/2
                if (distance >= 100):
                    p.ChangeDutyCycle(0)
                elif (distance <= 20):
                    p.ChangeDutyCycle(100)

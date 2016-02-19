import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 12
PWMpin = 7

GPIO.setup(PWMpin, GPIO.OUT)
p = GPIO.PWM(PWMpin,100)

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
                distance=duration*(34000/2)
                if ((distance >= 100) and (distance <= 4000)):
                    p.ChangeDutyCycle(0)
                if ((distance >= 90) and (distance <= 99)):
                    p.ChangeDutyCycle(1)
                if ((distance >= 80) and (distance <= 89)):
                    p.ChangeDutyCycle(5)
                if ((distance >= 70) and (distance <= 79)):
                    p.ChangeDutyCycle(10)
                if ((distance >= 60) and (distance <= 69)):
                    p.ChangeDutyCycle(20)
                if ((distance >= 50) and (distance <= 59)):
                    p.ChangeDutyCycle(35)
                if ((distance >= 40) and (distance <= 49)):
                    p.ChangeDutyCycle(55)
                if ((distance >= 0) and (distance <= 39)):
                    p.ChangeDutyCycle(100)
                print distance

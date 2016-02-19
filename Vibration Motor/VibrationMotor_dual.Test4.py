import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TRIG1 = 11
ECHO1 = 12

TRIG2 = 15
ECHO2 = 18

PWMpin = 7

GPIO.setup(PWMpin, GPIO.OUT)
p = GPIO.PWM(PWMpin,100)

p.start(0)
timeout = 0.020

while 1:
        GPIO.setup(TRIG1, GPIO.OUT)
        #cleanup output
        GPIO.output(TRIG1, 0)
        time.sleep(0.000002)

        GPIO.setup(TRIG2, GPIO.OUT)
        #cleanup output
        GPIO.output(TRIG2, 0)
        time.sleep(0.000002)
                
        #send signal
        GPIO.output(TRIG1, 1)
        time.sleep(0.000005)
        GPIO.output(TRIG1, 0)
        GPIO.setup(ECHO1, GPIO.IN)

        GPIO.output(TRIG2, 1)
        time.sleep(0.000005)
        GPIO.output(TRIG2, 0)
        GPIO.setup(ECHO2, GPIO.IN)
        
        goodread=True
        watchtime=time.time()
        while (GPIO.input(ECHO1)== 0 and goodread):
                starttime=time.time()
                if (starttime-watchtime > timeout):
                        goodread=False

        if goodread:
                watchtime=time.time()
                while (GPIO.input(ECHO1)== 1 and goodread):
                        endtime=time.time()
                        if (endtime-watchtime > timeout):
                                goodread=False

        goodread=True
        watchtime2=time.time()
        while (GPIO.input(ECHO2)== 0 and goodread):
                starttime2=time.time()
                if (starttime2-watchtime2 > timeout):
                        goodread=False

        if goodread:
                watchtime2=time.time()
                while (GPIO.input(ECHO2)== 1 and goodread):
                        endtime2=time.time()
                        if (endtime2-watchtime2 > timeout):
                                goodread=False
        
        if goodread:
                duration=endtime-starttime
                duration2=endtime2-starttime2
                distance=duration*(34000/2)
                distance2=duration2*(34000/2)
                '''if ((distance >= 100) and (distance <= 4000)):
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
                    p.ChangeDutyCycle(100)'''
                print 'distance1: ', distance
                print 'distance2: ', distance2

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

PWMser = 13

GPIO.setup(PWMser, GPIO.OUT)

p_ser = GPIO.PWM(PWMser,50)

p_ser.start(0)

try:
   while True:
       # Turn 0 degrees (intial)
       p_ser.ChangeDutyCycle(7.5)
       time.sleep(1)

       # Turn 90 degrees
       p_ser.ChangeDutyCycle(12.5)
       time.sleep(1)

       # Turn 0 degrees (intial)
       p_ser.ChangeDutyCycle(7.5)
       time.sleep(1)

       # Turn -90 degrees
       p_ser.ChangeDutyCycle(2.5)
       time.sleep(1)
         
except KeyboardInterrupt:
   pass

p_ser.stop()

GPIO.cleanup()

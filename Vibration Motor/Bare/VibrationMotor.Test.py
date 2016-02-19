import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

PWMpin = 7

GPIO.setup(PWMpin, GPIO.OUT)

p = GPIO.PWM(PWMpin,207)

p.start(0)

try:
   while True:
      for i in range(100):
         p.ChangeDutyCycle(i)
         time.sleep(0.02)
      for i in range(100):
         p.ChangeDutyCycle(100-i)
         time.sleep(0.02)
except KeyboardInterrupt:
   pass

p.stop()

GPIO.cleanup()

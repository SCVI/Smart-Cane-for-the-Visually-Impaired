import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

PWMpin = 7

GPIO.setup(PWMpin, GPIO.OUT)

p = GPIO.PWM(PWMpin,100)

p.start(0)

try:
   while True:
      p.ChangeDutyCycle(1)
      time.sleep(2)
      p.ChangeDutyCycle(0)
      time.sleep(2)
except KeyboardInterrupt:
   pass

p.stop()

GPIO.cleanup()

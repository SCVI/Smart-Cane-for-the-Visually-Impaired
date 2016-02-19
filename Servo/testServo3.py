import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

but_ser = 16 #pin of the button for the servo routine
PWMser = 13 #pin of the PWM for base servo

try:
   while True:
      def TurnServo():

         GPIO.setup(PWMser, GPIO.OUT)
         p_ser = GPIO.PWM(PWMser,50)
         p_ser.start(0)
         
         # Turn 90 degrees
         p_ser.ChangeDutyCycle(12.5)
         time.sleep(2)
         # Turn -90 degrees
         p_ser.ChangeDutyCycle(2.5)
         time.sleep(2)
         # Turn 0 degrees (intial)
         p_ser.ChangeDutyCycle(7.5)
         time.sleep(2)
         
         p_ser.stop

      def main():
         GPIO.setup(but_ser, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
         
         option =  True
         while (option):
            if (GPIO.input(but_ser) == 1):
               print "SERVO ROUTINE STARTED"
               TurnServo()
               time.sleep(0.2)
               option =  False
            else:
               time.sleep(0.2)
               print "waiting"
      main()
         
except KeyboardInterrupt:
   pass

GPIO.cleanup()

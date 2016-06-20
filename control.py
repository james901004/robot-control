# import modules
import time 
import RPi.GPIO as GPIO

#set up pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

p1 = GPIO.PWM(11,1000)
p1.start(10)
time(0.2)
p1.ChangeDutyCycle(20)
time(0.2)
p1.ChangeDutyCycle(20)
time(0.2)
p1.ChangeDutyCycle(30)
time(0.2)
p1.ChangeDutyCycle(40)
time(0.2)
p1.ChangeDutyCycle(50)
time(0.2)
p1.ChangeDutyCycle(60)
time(0.2)
p1.ChangeDutyCycle(70)
time(0.2)
p1.ChangeDutyCycle(80)
time(0.2)
p1.ChangeDutyCycle(90)
time(0.2)
p1.ChangeDutyCycle(100)

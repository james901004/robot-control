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
P1.start(10)

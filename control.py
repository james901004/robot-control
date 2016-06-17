# import modules
import time 
import RPi.GPIO as GPIO

#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)


while true:
  try:
    bottns=
    
    # go forward
    if(bottons & #forward)
    GPIO.output(11, True)
    GPIO.output(12, True)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(3)
    
    # go left
    if(bottons & #left)
    GPIO.output(11, False)
    GPIO.output(12, True)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(3)
    
    #go right
    if(bottons & #right)
    GPIO.output(11, True)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(3)
    
    #go backward
    GPIO.output(11, True)
    GPIO.output(12, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    time.sleep(3)

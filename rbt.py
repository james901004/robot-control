import RPi.GPIO as io
io.setmode(io.BOARD)
import sys, tty, termios, time
import cwiid
import math

# These two blocks of code configure the PWM settings for
# the two DC motors on the RC car. It defines the two GPIO
# pins used for the input, starts the PWM and sets the
# motors' speed to 0

#Right motor setting
motor1_in1_pin = 11
motor1_in2_pin = 12
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)
motor1 = io.PWM(11,1000)
motor1.start(0)
motor1.ChangeDutyCycle(0)

#Left motor setting
motor2_in1_pin = 13
motor2_in2_pin = 15
io.setup(motor2_in1_pin, io.OUT)
io.setup(motor2_in2_pin, io.OUT)
motor2 = io.PWM(13,1000)
motor2.start(0)
motor2.ChangeDutyCycle(0)

#LED setup
io.setup(32, io.OUT)
io.output(32, True)

# This section of code defines the methods used to determine
# whether a motor needs to spin forward or backwards. The
# different directions are acheived by setting one of the
# GPIO pins to true and the other to false. If the status of
# both pins match, the motor will not turn.
def motor1_forward():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, False)

def motor1_reverse():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, True)

def motor2_forward():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, False)

def motor2_reverse():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, True)


# Setting the PWM pins to false so the motors will not move
# until the user presses the first key
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)

#dutycycle
dutycycle = 5
k = 0.55
n = 1
time1 = time.time()
#wii remote
button_delay = 0.1
print 'press 1+2 on your wii remote now ...'
time.sleep(1)
wii = None
i = 2
while not wii:
 try:
     wii=cwiid.Wiimote()
 except RuntimeError:
     if (i>50):
         print "Error opening wiimote connection"
         io.output(32, False)
         io.cleanup()
         quit()
         break
     print "attempt" + str(i)
     i += 1
  
print 'Wii Remote connected...\n'
io.output(32, False)
wii.rumble = 1
time.sleep(1)
wii.rumble = 0
print 'Press PLUS and MINUS together to disconnect and quit.\n'
wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']
  
  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    io.cleanup()
    exit(wii)  

  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time2 = time.time()
    timedelta = time2 - time1
    if timedelta > 0.5:
     dutycycle = 5
    else:
     dutycycle = dutycycle
    motor1_forward()
    motor2_reverse()
    motor1.ChangeDutyCycle(dutycycle)
    motor2.ChangeDutyCycle(dutycycle * k)
    time.sleep(button_delay)
    time1 = time.time()

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time2 = time.time()
    timedelta = time2 - time1
    if timedelta > 0.5:
     dutycycle = 5
     n = 1
    else:
     dutycycle = dutycycle
    n += 1
    dutycycle = 20 * (1 - math.exp(-n))
    motor1_reverse()
    motor2_forward()
    motor1.ChangeDutyCycle(dutycycle)
    motor2.ChangeDutyCycle(dutycycle * k )
    time.sleep(button_delay)
    time1 = time.time()


  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    time2 = time.time()
    timedelta = time2 - time1
    if timedelta > 0.5:
     dutycycle = 5
    else:
     dutycycle = dutycycle
    if dutycycle > 10:
        motor1_forward()
        motor2_reverse()
        motor1.ChangeDutyCycle(dutycycle)
        motor2.ChangeDutyCycle(dutycycle * k * 0.3)
    else:
        motor1_reverse()
        motor2_reverse()
        motor1.ChangeDutyCycle(dutycycle)
        motor2.ChangeDutyCycle(dutycycle * k)
    time.sleep(button_delay)
    time1 = time.time()

    
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time2 = time.time()
    timedelta = time2 - time1
    if timedelta > 0.5:
     dutycycle = 5
    else:
     dutycycle = dutycycle
    if dutycycle > 10:
       motor1_reverse()
       motor2_forward()
       motor1.ChangeDutyCycle(dutycycle * 0.3)
       motor2.ChangeDutyCycle(dutycycle * k)
    else:
       motor1_forward()
       motor2_forward()
       motor1.ChangeDutyCycle(dutycycle)
       motor2.ChangeDutyCycle(dutycycle * k)
    time.sleep(button_delay)
    time1 = time.time()

  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(0.1)
    if dutycycle > 5:
        dutycycle = dutycycle - 5
    else:
        dutycycle = 5
    
  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(0.1) 
    if dutycycle < 20:
        dutycycle = dutycycle + 5
    else:
        dutycycle = 20

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)
    dutycycle = 3

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
  else:
    motor1.ChangeDutyCycle(0)
    motor2.ChangeDutyCycle(0)



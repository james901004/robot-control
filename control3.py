import RPi.GPIO as io
io.setmode(io.BOARD)
import sys, tty, termios, time
import cwiid

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

# Defining the GPIO pins that will be used for the LEDs on
# the RC car and setting the output to false

#io.setup(18, io.OUT)
#io.output(18, False)

#io.setup(23, io.OUT)
#io.output(23, False)

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files 
# It will then return the pressed key as a variable
#def getch():
#    fd = sys.stdin.fileno()
#    old_settings = termios.tcgetattr(fd)
#    try:
#       tty.setraw(sys.stdin.fileno())
#        ch = sys.stdin.read(1)
#    finally:
#        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#    return ch

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

# This method will toggle the lights on/off when the user
# presses a particular key. It will then change the status
# of the lights so it will know whether to turn them on or
# off when it is next called.
#def toggleLights():

#    global lightStatus

#    if(lightStatus == False):
#        io.output(18, True)
#        io.output(23, True)
#        lightStatus = True
#    else:
#        io.output(18, False)
#        io.output(23, False)
 #       lightStatus = False

# This method will toggle the direction of the steering
# motor. The method will determine whether the user wants
# to turn left or right depending on the key they press and
# then make the appropriate adjustment. It works as a toggle
# because the program cannot read multiple pressed keys at
# the same time. The possible positions of the wheels are
# "right", "centre" and "left". It will then update the
# status of the wheel to access next time it is called.
#def toggleSteering(direction):

#    global wheelStatus

#    if(direction == "right"):
#        if(wheelStatus == "centre"):
#            motor1_forward()
#            motor1.ChangeDutyCycle(99)
#            wheelStatus = "right"
#        elif(wheelStatus == "left"):
#            motor1.ChangeDutyCycle(0)
#            wheelStatus = "centre"

#    if(direction == "left"):
#        if(wheelStatus == "centre"):
#            motor1_reverse()
#            motor1.ChangeDutyCycle(99)
#            wheelStatus = "left"
#        elif(wheelStatus == "right"):
#            motor1.ChangeDutyCycle(0)
#            wheelStatus = "centre"

# Setting the PWM pins to false so the motors will not move
# until the user presses the first key
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)

# Global variables for the status of the lights and steering
#lightStatus = False
#wheelStatus = "centre"

# Instructions for when the user has an interface
#print("w/s: acceleration")
#print("a/d: steering")
#print("l: lights")
#print("use w/s/a/d to control")
#print("x: exit")

# Infinite loop that will not end until the user presses the
# exit key
#while True:
    # Keyboard character retrieval method is called and saved
    # into variable
#    char = getch()

    # The car will drive forward when the "w" key is pressed
#    if(char == "w"):
#        motor1_forward()
#        motor2_forward()
#        motor1.ChangeDutyCycle(99)
#        motor2.ChangeDutyCycle(99)

    # The car will reverse when the "s" key is pressed
#    if(char == "s"):
#        motor1_reverse()
#        motor2_reverse()
#        motor1.ChangeDutyCycle(99)
#        motor2.ChangeDutyCycle(99)

    # The "a" key will toggle the steering left
#    if(char == "a"):
        #toggleSteering("left")
#        turn_left()

    # The "d" key will toggle the steering right
#    if(char == "d"):
        #toggleSteering("right")
#        turn_right

    # The "l" key will toggle the LEDs on/off
    #if(char == "l"):
    #    toggleLights()

    # The "x" key will break the loop and exit the program
#    if(char == "x"):
#        print("Program Ended")
#        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
#    motor1.ChangeDutyCycle(0)
#    motor2.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
#    char = ""
#dutycycle
dutycycle = 10
#wii remote
button_delay = 0.1
print 'press 1+2 on your wii remote now ...'
time.sleep(1)
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()
  
print 'Wii Remote connected...\n'
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
    exit(wii)  
    
  time1 = time()

  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time2 = time()
    if time2 - time1 > 2:
     dutycycle = 10
    else:
     dutycycle = dutycycle
    motor1_forward()
    motor2_reverse()
    motor1.ChangeDutyCycle(dutycycle)
    motor2.ChangeDutyCycle(dutycycle)
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time2 = time()
    if time2 - time1 > 2:
     dutycycle = 10
    else:
     dutycycle = dutycycle
    motor1_reverse()
    motor2_forward()
    motor1.ChangeDutyCycle(dutycycle)
    motor2.ChangeDutyCycle(dutycycle)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    time2 = time()
    if time2 - time1 > 2:
     dutycycle = 10
    else:
     dutycycle = dutycycle
    motor1_forward()
    motor2_forward()
    motor1.ChangeDutyCycle(dutycycle)
    motor2.ChangeDutyCycle(dutycycle)
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time2 = time()
    if time2 - time1 > 2:
     dutycycle = 10
    else:
     dutycycle = dutycycle
    motor1_reverse()
    motor2_reverse()
    motor1.ChangeDutyCycle(dutycycle)
    motor2.ChangeDutyCycle(dutycycle)
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(0.5) 
    if dutycycle < 100:
        dutycycle = dutycycle + 10
    else:
        dutycycle = 100

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(0.5)
    if dutycycle > 10:
        dutycycle = dutycycle - 10
    else:
        dutycycle = 10

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)
    dutycycle = 10

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

# Program will cease all GPIO activity before terminating
io.cleanup()

# robot-control

press 1+2 to setup linkage between pi and wii remote when the LED is up
up button: go forward and speed up while you pressing the button. stop automatically when the distance is too close (smaller than 5 cm)
right button: spot turn right in low speed(pwm<10),turn right and go forward in high speed(pwm>10)
left button: spot turn left in low speed(pwm<10),turn left and go forward in high speed(pwm>10)
down button: go back
A button: reset to low speed(pwm=5)
1 button: speed down
2 button: speed up

press -&+ to disconnect from PI

remove the file: rm -rf robot-control
download the file: git clone https://github.com/james901004/robot-control
change autostart sudo nano /etc/rc.local

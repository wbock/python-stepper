from Stepper import stepper
from RobotEyes import robotEyes
from time import sleep


#stepper variables
#[stepPin, directionPin, enablePin]
leftEye = stepper([22, 21, 23])
rightEye = stepper([36, 35, 37])

#robot eyes with two steppers
robi = robotEyes(leftEye, rightEye)

#define wait-time between steps:
#use 0.001 for Raspberry Pi 3
#use 0.1 for Jetson Nano
robi.set_speed(0.001);

##demo loop
#   function overview for Robi:
#   lookLeft(), lookRight(), lookUp(), lookDown(),
#   rollEyes(), crossEyes()
#   (Steppers release position after lookDown() - stay locked otherwise)
#
#   pause between actions with: sleep(<seconds>);
#
##

robi.lookLeft();
sleep(1);
robi.lookUp();
sleep(1);
robi.rollEyes();
robi.lookDown();
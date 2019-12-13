##Robot eyes - Stepper home position is down
#
#   Movement functions:
#   lookLeft, lookRight, lookUp, lookDown
#   crossEyes - looks towards the middle
#   rollEyes - spins 360 degrees from current position
#   set_speed - wait time between steps = 0.000001/speed
##

class robotEyes():
    posLeft = "down"
    posRight = "down"

    def __init__(self, stepper1, stepper2):
        self.leftEye = stepper1
        self.rightEye = stepper2

    def set_speed(self, speed):
        self.leftEye.set_speed(speed);
        self.rightEye.set_speed(speed);

    def set_stayOn(self, stayOn):
        self.leftEye.set_stayOn(stayOn);
        self.rightEye.set_stayOn(stayOn);

    def lookLeft(self):
        self.set_stayOn(True);

        if self.posLeft == "left":
            self.leftEye.set_instructions(0, "left");
        elif self.posLeft == "right":
            self.leftEye.set_instructions(1600, "left");
        elif self.posLeft == "up":
            self.leftEye.set_instructions(800,"right");
        elif self.posLeft == "down":
            self.leftEye.set_instructions(800,"left");

      
        if self.posLeft == "left":
            self.rightEye.set_instructions(0, "left");
        elif self.posRight == "right":
            self.rightEye.set_instructions(1600, "left");
        elif self.posRight == "up":
            self.rightEye.set_instructions(800,"right");
        elif self.posRight == "down":
            self.rightEye.set_instructions(800,"left");

            
        self.leftEye.go();
        self.rightEye.goJoin();

        self.posLeft = "left";
        self.posRight = "left";
        self.set_stayOn(True);


    def lookRight(self):
        self.set_stayOn(True);
        
        if self.posLeft == "left":
            self.leftEye.set_instructions(1600, "right");
        elif self.posRight == "right":
            self.rightEye.set_instructions(0, "left");
        elif self.posLeft == "up":
            self.leftEye.set_instructions(800,"left");
        elif self.posLeft == "down":
            self.leftEye.set_instructions(800,"right");

        
        if self.posRight == "left":
            self.rightEye.set_instructions(1600, "right");
        elif self.posRight == "right":
            self.rightEye.set_instructions(0, "left");
        elif self.posRight == "up":
            self.rightEye.set_instructions(800,"left");
        elif self.posRight == "down":
            self.rightEye.set_instructions(800,"right");

            
        self.leftEye.go();
        self.rightEye.goJoin();

        self.posLeft = "right";
        self.posRight = "right";


    def lookUp(self):
        self.set_stayOn(True);

        if self.posLeft == "left":
            self.leftEye.set_instructions(800, "left");
        elif self.posLeft == "right":
            self.leftEye.set_instructions(800,"right");
        elif self.posRight == "up":
            self.leftEye.set_instructions(0,"left");
        elif self.posLeft == "down":
            self.leftEye.set_instructions(1600,"left");

        
        if self.posRight == "left":
            self.rightEye.set_instructions(800, "left");
        elif self.posRight == "right":
            self.rightEye.set_instructions(800,"right");
        elif self.posRight == "up":
            self.rightEye.set_instructions(0,"left");
        elif self.posRight == "down":
            self.rightEye.set_instructions(1600,"right");

            
        self.leftEye.go();
        self.rightEye.goJoin();

        self.posLeft = "up";
        self.posRight = "up";

        
    def lookDown(self):
        self.set_stayOn(False);
        
        if self.posLeft == "left":
            self.leftEye.set_instructions(800, "right");
        elif self.posLeft == "right":
            self.leftEye.set_instructions(800,"left");
        elif self.posLeft == "up":
            self.leftEye.set_instructions(1600,"right");
        elif self.posRight == "down":
            self.leftEye.set_instructions(0,"right");

        
        if self.posRight == "left":
            self.rightEye.set_instructions(800, "right");
        elif self.posRight == "right":
            self.rightEye.set_instructions(800,"left");
        elif self.posRight == "up":
            self.rightEye.set_instructions(1600,"left");
        elif self.posRight == "down":
            self.rightEye.set_instructions(0,"right");

            
        self.leftEye.go();
        self.rightEye.goJoin();

        self.posLeft = "down";
        self.posRight = "down";


    def crossEyed(self):
        self.set_stayOn(True);
          
        if self.posLeft == "left":
            self.leftEye.set_instructions(0, "right");
        elif self.posLeft == "right":
            self.leftEye.set_instructions(1600,"left");
        elif self.posLeft == "up":
            self.leftEye.set_instructions(800,"right");
        elif self.posLeft == "down":
            self.leftEye.set_instructions(800,"left");

        
        if self.posRight == "left":
            self.rightEye.set_instructions(1600, "right");
        elif self.posRight == "right":
            self.rightEye.set_instructions(0,"left");
        elif self.posRight == "up":
            self.rightEye.set_instructions(800,"left");
        elif self.posRight == "down":
            self.rightEye.set_instructions(800,"right");

            
        self.leftEye.go();
        self.rightEye.goJoin();

        self.posLeft = "left";
        self.posRight = "right";



    def rollEyes(self):
        self.leftEye.set_instructions(3200, "right");
        self.rightEye.set_instructions(3200, "right");
        
        self.leftEye.go();
        self.rightEye.goJoin();

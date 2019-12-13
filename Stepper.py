#CURRENT APPLICATION INFO
#200 steps/rev
#12V, 350mA
#Big Easy driver = 1/16 microstep mode
#Turn a 200 step motor left one full revolution: 3200

import threading #address motors seperately
from time import sleep
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO
#import exitHandler #uncomment this and line 58 if using exitHandler


class stepper():
        steps = 0
        dir = 'right'
		#default wait-time between steps:
		#use 0.001 for Raspberry Pi 3
		#use 0.1 for Jetson Nano
        speed = 0.001
        stayOn = False
        pins = []

        def __init__(self, pins):
                #setup pins
                self.pins = pins
                
                #use the broadcom layout for the gpio
                gpio.setmode(gpio.BOARD)
                
                #set gpio pins
                gpio.setup(self.pins[0], gpio.OUT)
                gpio.setup(self.pins[1], gpio.OUT)
                gpio.setup(self.pins[2], gpio.OUT)
                
                #set enable to high (i.e. power is NOT going to the motor)
                gpio.output(self.pins[2], True)
                
                #print("Stepper initialized (step=" + self.stepPin + ", direction=" + self.directionPin + ", enable=" + self.enablePin + ")")

        
        #clears GPIO settings
        def cleanGPIO(self):
                gpio.cleanup()
                

        #run thread consecutively
        def go(self):
                thread = stepper_thread(self.steps, self.dir, self.speed, self.stayOn, self.pins)
                thread.start();

        #run thread sequentially
        def goJoin(self):
                thread = stepper_thread(self.steps, self.dir, self.speed, self.stayOn, self.pins)
                thread.start();
                thread.join();
                

        def set_instructions(self, steps, dir):
                self.steps = steps
                self.dir = dir

        def set_speed(self, speed):
                self.speed = speed

        def set_stayOn(self, stayOn):
                self.stayOn = stayOn
                


class stepper_thread (threading.Thread):
        #instantiate stepper 
        #pins = [stepPin, directionPin, enablePin]
        def __init__(self, steps, dir, speed, stayOn, pins):
                threading.Thread.__init__(self)
                self.steps = steps
                self.dir = dir
                self.speed = speed
                self.stayOn = stayOn
                self.stepPin = pins[0]
                self.directionPin = pins[1]
                self.enablePin = pins[2]
	
        #step the motor
        # steps = number of steps to take
        # dir = direction stepper will move
        # speed = defines the denominator in the waitTime equation: waitTime = 0.000001/speed. As "speed" is increased, the waitTime between steps is lowered
        # stayOn = defines whether or not stepper should stay "on" or not. If stepper will need to receive a new step command immediately, this should be set to "True." Otherwise, it should remain at "False."
        def run(self):
                #set enable to low (i.e. power IS going to the motor)
                gpio.output(self.enablePin, False)
                
                #set the output to true for left and false for right
                turnLeft = True
                if (self.dir == 'right'):
                        turnLeft = False;
                elif (self.dir != 'left'):
                        print("STEPPER ERROR: no direction supplied")
                        return False
                gpio.output(self.directionPin, turnLeft)

                stepCounter = 0
        
                waitTime = 0.000001/self.speed #waitTime controls speed

                while stepCounter < self.steps:
                        #gracefully exit if ctr-c is pressed
                        #exitHandler.exitPoint(True) #exitHandler.exitPoint(True, cleanGPIO)

                        #turning the gpio on and off tells the easy driver to take one step
                        gpio.output(self.stepPin, True)
                        gpio.output(self.stepPin, False)
                        stepCounter += 1

                        #wait before taking the next step thus controlling rotation speed
                        sleep(waitTime)
                
                if (self.stayOn == False):
                        #set enable to high (i.e. power is NOT going to the motor)
                        gpio.output(self.enablePin, True)

                print("stepperDriver complete (turned " + self.dir + " " + str(self.steps) + " steps)")

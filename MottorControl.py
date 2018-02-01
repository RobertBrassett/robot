import time
import RPi.GPIO

#Executes all necessary functions to rotate the antenna of a given difference in angle and speed
#INPUTS:    degree -> difference in angle that the mottor must turn, left turn is negative degrees and right turn is positive
#           speed -> wait time between each step, must be larger than 0.0014s or the function will correct this
#FUNCTIONS USED:    checkSpeed()
#                   stepCalc()
#                   directionCalc()
#                   stepMotion()

def ChangeAntennaAngle (degree, speed):
    directionCalc(degree)
    stepMotion(stepCalc(degree), checkSpeed(speed))    
    return


#Checks the speed
#INPUT: s - > speed
def checkSpeed(s):
    if speed < 0.0007 :
        speed = 0.0007
    return speed


#Calculates steps needed
#INPUTS:    d -> difference in degrees
def stepCalc(d):
    steps = (abs(d)/360) * 19985 
    return steps


#Claculates direction
#INPUTS:    d -> difference in degrees 
def directionCalc(d):
    if degree < 0:
        GPIO.output(DIR, True)
    elif degree > 0:
        GPIO.output(DIR, False)


#Executes motion of Antenna
#INPUTS:    steps -> steps the mottor will take
#           speed -> time delay between steps
def stepMotion(steps, speed):
    while StepCounter < steps:
        GPIO.output(STEP,True)
        time.sleep(speed)
        GPIO.output(STEP,False)
        StepCounter += 1
        time.sleep(speed)


#main
#--------------------------------------------------------
GPIO.setmode(GPIO.BCM)
DIR = 23
STEP = 24
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

ChangeAntennaAngle(degree,speed)

GPIO.cleanup()

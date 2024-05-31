import board
import time
import digitalio, pwmio
from adafruit_motor import stepper, servo

class MotorAxes:
    motorX: stepper.StepperMotor = None
    motorY: stepper.StepperMotor = None
    currPos: tuple[float] = None
    def __init__(self, coilsX, coilsY, currPos=(0,0)):
        self.motorX = stepper.StepperMotor(*coilsX, microsteps=None)
        self.motorY = stepper.StepperMotor(*coilsY, microsteps=None)
        self.currPos = currPos
    
    def moveDistance(self, Xdist, Ydist):
        for i in range(Xdist):
            self.motorX.onestep()
        for i in range(Ydist):
            self.motorY.onestep()

    def moveTo(self, X, Y):
        Xdist = X - self.currPos[0]
        Ydist = Y - self.currPos[1]
        self.moveDistance(Xdist, Ydist)


coilsX = (
    digitalio.DigitalInOut(board.D9),
    digitalio.DigitalInOut(board.D10),
    digitalio.DigitalInOut(board.D11),
    digitalio.DigitalInOut(board.D12)
)

coilsY = (
    digitalio.DigitalInOut(board.D4),
    digitalio.DigitalInOut(board.D5),       
    digitalio.DigitalInOut(board.D6),
    digitalio.DigitalInOut(board.D7)
)

for coil in coilsX, coilsY:
    coil.direction = digitalio.Direction.OUTPUT
axes = MotorAxes(coilsX, coilsY)

servoPin = pwmio.PWMOut(board.D2)
penServo = servo.Servo(servoPin)

def raiseLowerPen(penDown):
    if penDown == True:
        penServo.angle = 0
    else:
        penServo.angle = 45
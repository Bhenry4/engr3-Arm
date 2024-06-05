import runMotor # motor logic in other file

totalXSteps = 0
totalYSteps = 0

def f(x):
        return x**2

def findPoints(r, f): # finds the values of points in a given range (interpeted as xx.x) with the given function
    points = []
    for x in r:
        try:
            points.append((x*0.1, f(x*0.1)))
        except:
            pass # returns nothing for divide by zero, etc. (discontinuities)
    return points

def autoFit(points): # finds the minimum and maximum y-values for the given x-range (using the points list)
    ymax = 0
    ymin = 0
    for point in points:
        if point[1] > ymax:
            ymax = point[1]
        if point[1] < ymin:
            ymin = point[1]
    return ymax, ymin

def graphPoint(Xunits, Yunits, stepsPerXUnit, stepsPerYUnit, penDown): # Takes a point in graph units and converts it to motor steps, then calls the motor module to move the motors
    Xsteps = Xunits * stepsPerXUnit
    Ysteps = Yunits * stepsPerYUnit
    runMotor.axes.moveTo(Xsteps, Ysteps)
    runMotor.raiseLowerPen(penDown)

# this block uses the functions to find the points, figure out the graph unit to motor step conversion, then graph it
points = findPoints(range(-100, 100+1), f)
print(points)
ymax, ymin = autoFit(points)
print(ymax, ymin)
stepsPerXUnit = totalXSteps/20
stepsPerYUnit = totalYSteps/(ymax-ymin)
print(stepsPerYUnit, stepsPerXUnit)

for point in points:
    graphPoint(point[0], point[1], stepsPerXUnit, stepsPerYUnit, False)

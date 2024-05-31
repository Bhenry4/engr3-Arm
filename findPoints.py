import runMotor

totalXSteps = 0
totalYSteps = 0

def f(x):
        return x**2

def findPoints(r, f):
    points = []
    for x in r:
        try:
            points.append((x*0.1, f(x*0.1)))
        except:
            pass
    return points

def autoFit(points):
    ymax = 0
    ymin = 0
    for point in points:
        if point[1] > ymax:
            ymax = point[1]
        if point[1] < ymin:
            ymin = point[1]
    return ymax, ymin

def graphPoint(Xunits, Yunits, stepsPerXUnit, stepsPerYUnit, penDown):
    Xsteps = Xunits * stepsPerXUnit
    Ysteps = Yunits * stepsPerYUnit
    runMotor.axes.moveTo(Xsteps, Ysteps)
    runMotor.raiseLowerPen(penDown)

points = findPoints(range(-100, 100+1), f)
print(points)
ymax, ymin = autoFit(points)
print(ymax, ymin)
stepsPerXUnit = totalXSteps/20
stepsPerYUnit = totalYSteps/(ymax-ymin)
print(stepsPerYUnit, stepsPerXUnit)

for point in points:
    graphPoint(point[0], point[1], stepsPerXUnit, stepsPerYUnit, False)
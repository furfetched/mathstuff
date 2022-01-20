import math

mathInput = float(input("\nThis is a sin/cos/tan to deg/rad calculator\nEnter trig value\n"))
typeInput = input("\nEnter trig function type\n")

if typeInput == "sin":
    x = math.asin(mathInput)
elif typeInput == "cos":
    x = math.acos(mathInput)
elif typeInput == "tan":
    x = math.atan(mathInput)

def degree(x):
    pi = math.pi
    degree = (x*180)/pi
    return degree

print(f"\nDegree is {degree(x)}\nAmount of radians is {x}")
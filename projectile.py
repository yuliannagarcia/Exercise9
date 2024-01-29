import math as m    # imports math module as m

theta = m.radians(80)  # converts degrees to rads
g = 9.81
# acceleration due to gravity is a constant, tf doesn't need user input
v = float(input("Enter the initial velocity (m/s):"))
# typecasts initial velocity (m/s) as float
x = float(input("Enter the horizontal distance travelled (m):"))
# horizontal distance
y = float(input("Enter the height of the barrel (m):"))
# barrel height m
ang = m.radians(float((input("Enter elevation angle in degrees: "))))
# converts user input from degrees to radians, then typecasts result as float

result = y + (x * m.tan(ang)) - ((g * x ** 2) / (2 * (v * m.cos(ang))**2))

print(f"The height of the projectile was {(round(result, 2))} m")
# f string concatenates dif types together making the code more readable
# {round(result,2))} rounds the contents of 'result' var
# to 2 decimal places
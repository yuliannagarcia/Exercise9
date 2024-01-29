# Import math functions needed
from math import pi, tan, cos

# values
g = 9.81  # acceleration due to gravity in m/s^2
yo = 1    # height of the barrel in meters
x = 0.5   # horizontal distance travelled in meters
deg = 80  # elevation angle in degrees
vo = 44   # initial velocity in m/s

# converts angle from degrees to radians. π radians is equivalent to 180 degrees.
theta = deg * (pi / 180)
print("Angle in radians:", theta)

# calculating the parts of the height equation

# the vertical part of the projectile's height, using the height of the barrel and the vertical
# displacement due to elevation.
vertical_motion = yo + x * tan(theta)
# tan(theta) = the tangent of the elevation angle
print("Vertical motion:", vertical_motion)

# the horizontal part of the projectile's height, using the horizontal displacement and the gravity
# on horizontal motion.
horizontal_motion = (g * x**2) / (2 * (vo * cos(theta)) ** 2)
# the cosine of the elevation angle theta. **2= to the power of two (equation)
print("Horizontal motion:", horizontal_motion)

# calculates the total height of the projectile by subtracting the horizontal motion part from the vertical
# motion part
y = vertical_motion - horizontal_motion  # the total height reached by the projectile
print("Projectile height:", y, "m")  # print the height of the projectile

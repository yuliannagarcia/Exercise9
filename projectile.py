# Import necessary math functions
from math import pi, tan, cos

# Given values
g = 9.81  # Acceleration due to gravity in m/s^2
yo = 1    # Height of the barrel in meters
x = 0.5   # Horizontal distance travelled in meters
elevation_degrees = 80  # Elevation angle in degrees
initial_velocity = 44   # Initial velocity in m/s

# Convert angle from degrees to radians
elevation_radians = elevation_degrees * (pi / 180)  # Convert elevation angle to radians
print("Elevation angle in radians:", elevation_radians)

# Calculate the components of the height equation
vertical_motion = yo + x * tan(elevation_radians)  # Calculate vertical motion component
print("Vertical motion component:", vertical_motion)

horizontal_motion = (g * x**2) / (2 * (initial_velocity * cos(elevation_radians))**2)  # Calculate horizontal motion component
print("Horizontal motion component:", horizontal_motion)

# Calculate the height of the projectile
height = vertical_motion - horizontal_motion  # Calculate total height of the projectile
print("Height of the projectile:", height, "m")  # Print the height of the projectile

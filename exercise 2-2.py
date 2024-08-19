import math

radius_string = input("Enter the radius of the circle: ")
radius_float = float(radius_string)
print(f"The area of the circle with radius {radius_float} is {math.pi*radius_float**2}")

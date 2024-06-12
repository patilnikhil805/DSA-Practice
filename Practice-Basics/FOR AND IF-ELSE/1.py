# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# r = 1.1
# area = 3.14 * r * r

# print("Area of Circle is =" , area)

from math import pi

r = (float(input("Enter the radius of the circle : ")))

area = pi * r * r

print("The radius of the circle with radius " + str(r) + " is : " + str(area))
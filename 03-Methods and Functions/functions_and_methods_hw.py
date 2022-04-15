# Write a function that computes the volume of a sphere given its radius.

from cmath import pi

def vol(rad):
    volume = (4/3*(pi*rad**3))
    print(volume)

vol(2)

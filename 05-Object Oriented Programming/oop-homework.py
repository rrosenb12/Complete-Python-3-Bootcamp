# Problem 1
## Make a Line class method that accepts coordinates as a pair of tuples and returns the slope and distance of the line

from cmath import sqrt

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2 

    def distance(self):
        return sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)
    
    def slope(self):
        return ((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

# Problem 2
## Create a Cylinder class that calculates the volume and surface area

class Cylinder:

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius 
    
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height 

    def surface_area(self):
        return((2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * self.radius**2))

c = Cylinder(2,3)

print(c.surface_area())
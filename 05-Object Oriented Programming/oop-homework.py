#Problem 1
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

print(li.slope())
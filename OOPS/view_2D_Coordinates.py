"""
Write the OOP class to handle the following Scenarios
  1 A user can create and view the 2D coordinates
  2 A user can find out the distance between 2 coordinates
  3 A user can find  the distance of a coordinate from origin
  4 A user can check if a point lies on a given line
  5 A user can find the distance between a given 2D point and a given line
"""

class point:

    def __init__(self ,x,y):
        self.x_cod = x
        self.y_cod = y

    #1 A user can create and view the 2D coordinates
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    #2 A user can find out the distance between 2 coordinates
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

    #3 A user can find  the distance of a coordinate from origin
    def distance_from_origin(self):
        return self.euclidean_distance(point(0,0))

#4 A user can check if a point lies on a given line
class Line(point):

    def __init__(self,A,B,C):


        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return ' {}x + {}y + {}= 0 '.format(self.A,self.B,self.C)

    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lie on the line"




p1 = point(0,0)
p2 = point(10,10)

print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())

l1 = Line(1,1,-2)
p1 = point(1,1)
print(l1)
print(p1)

print(l1.point_on_line(p1))



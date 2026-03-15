"""
Write the OOP class to handle the following Scenarios
  1 A user can create and view the 2D coordinates
  2 A user can find out the distance between 2 coordinates
  3 A user can find  the distance of a coordinate from origin
  4 A user can find  the distance between a given 2D  point and a given line
"""

class point:

    def __init__(self ,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)



p1 = point(1,2)
p2 = point(3,4)

print(p1)
print(p2)

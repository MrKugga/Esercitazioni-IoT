from Ex1 import Point
from math import sqrt

class Line:

    def __init__(self, m= None, q= None):

        if m is not None and q is not None:
            self.m = m
            self.q = q
        else:
            self.exp = None

    def __repr__(self):
        return "Line()"

    def __str__(self):
        return f"Line: y = {self.m}x + {self.q}"

    def lineFromPoints(self, a, b):
        if isinstance(a, Point) and isinstance(b, Point):
            self.m = (b.y-a.y)/(b.x-a.x)
            self.q = -(b.y-a.y)/(b.x-a.x)*a.x + a.y
        else:
            raise ValueError(f'Invalid argument. {a} and {b} must be of type Point.')

    def distance(self, a):
        if isinstance(a, Point):
            dis = abs(a.y-(self.m*a.x+self.q))/sqrt(1+self.m**2)
            return dis
        else:
            raise ValueError

    def intersection(self, a):
        if isinstance(a, Line):
            i = Point((a.q - self.q)/(self.m - a.m), (a.q - self.q)/(self.m - a.m) + self.q)
            return i
        else:
            raise ValueError

if __name__ == "__main__":
    l = Line(3, 2)
    print(l)

    a = Point(0,1)
    b = Point(2,2)

    l.lineFromPoints(a, b)

    print(l)

    l = Line(1,0)
    a = Point(1,5)
    print(l.distance(a))

    m = Line(-1, 0)

    i = l.intersection(m)
    print(i)

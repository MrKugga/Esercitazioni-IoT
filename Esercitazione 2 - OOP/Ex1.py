from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point()"

    def __str__(self):
        return(f'({self.x},{self.y})')

    def distance(self, pnt):
        if isinstance(pnt, Point):
            dis = sqrt((self.x - pnt.x)**2+(self.y - pnt.y)**2)
            return dis
        else:
            raise ValueError(f'Invalid argument. {pnt} must be of type Point.')

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


if __name__ == "__main__":
    a = Point(7,1)
    b = Point(1,1)

    print(a.distance(b))

    a.move(2,2)
    print(a)

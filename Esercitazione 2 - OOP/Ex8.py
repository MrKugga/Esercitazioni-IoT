from math import pi

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2

    def baseArea(self):
        area = pi*self.radius**2
        return area

    def perimeter(self):
        perimeter = pi*self.diameter
        return perimeter

    def __str__(self):
        return f"Circle of diameter: {self.diameter}"


class Cylinder(Circle):
    def __init__(self, diameter, height):
        super().__init__(diameter)
        self.height = height

    def totalArea(self):
        tot = 2*self.baseArea()+self.perimeter()*self.height
        return tot

    def volume(self):
        volume = self.baseArea()*self.height
        return volume

    def __str__(self):
        return f"Cylinder of diameter {self.diameter} and height {self.height}"

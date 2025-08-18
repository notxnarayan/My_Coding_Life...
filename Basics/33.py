from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Area not defined for generic shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle:", 3.14 * self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Area of Triangle:", 0.5 * self.base * self.height)

Circ=Circle(5)
Circ.area()
rect = Rectangle(4, 6)
rect.area()
tria =Triangle(3, 8)
tria.area()

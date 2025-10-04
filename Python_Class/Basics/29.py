"""Write a program to create a class Rectangle that takes length and breadth as input and calculates:
Area
Perimeter"""

class Rect:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def calc(self):
        area = self.length * self.breadth
        peri = (2*self.length) + (2*self.breadth)
        print(f"Perimeter is {peri}, Area is {area}")

ln = int(input("Enter the length: "))
bn = int(input("Enter the breadth: "))
rect = Rect(ln,bn)
rect.calc()
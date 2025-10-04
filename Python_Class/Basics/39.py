class Cord:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __eq__(self, other):
        return self.x == other.x, self.y == other.y

    def __gt__(self, other):
        return self.x > other.x, self.y > other.y

    def __lt__(self, other):
        return self.x < other.x, self.y < other.y


    def __str__(self):
        return self.x, self.y

p1 = Cord(3,4)
p2 = Cord(3,4)
psum = p1+p2
pmul = p1*p2
psub = p1-p2
peq = p1==p2
pgt = p1>p2
plt = p1<p2

print()
from copy import copy, deepcopy

class Cord:
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("__init__ called")
        self.x = x
        self.y = y

    def __del__(self):
        print("__del__ called")

    def __str__(self):
        return f"Cord({self.x}, {self.y})"

    def __repr__(self):
        return f"Cord({self.x}, {self.y})"

    def __format__(self, spec):
        return f"({format(self.x, spec)}, {format(self.y, spec)})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other):
        return (self.x, self.y) >= (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Cord(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return Cord(other.x + self.x, other.y + self.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Cord(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return Cord(other.x - self.x, other.y - self.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Cord(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return Cord(other.x * self.x, other.y * self.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __truediv__(self, other):
        return Cord(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Cord(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Cord(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Cord(self.x ** other.x, self.y ** other.y)

    def __neg__(self):
        return Cord(-self.x, -self.y)

    def __pos__(self):
        return Cord(+self.x, +self.y)

    def __abs__(self):
        return Cord(abs(self.x), abs(self.y))

    def __invert__(self):
        return Cord(~self.x, ~self.y)

    def __int__(self):
        return int((self.x + self.y) / 2)

    def __float__(self):
        return float((self.x + self.y) / 2)

    def __bool__(self):
        return bool(self.x or self.y)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __setitem__(self, index, val):
        if index == 0:
            self.x = val
        elif index == 1:
            self.y = val

    def __delitem__(self, index):
        if index == 0:
            self.x = 0
        elif index == 1:
            self.y = 0

    def __contains__(self, item):
        return item in (self.x, self.y)

    def __iter__(self):
        return iter((self.x, self.y))

    def __next__(self):
        raise StopIteration

    def __enter__(self):
        print("__enter__ called")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called")

    def __call__(self, *args, **kwargs):
        print(f"Called with args={args}, kwargs={kwargs}")

    def __getattr__(self, name):
        print(f"__getattr__ for {name}")
        return None

    def __setattr__(self, name, value):
        print(f"__setattr__ for {name} = {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"__delattr__ for {name}")
        super().__delattr__(name)

    def __copy__(self):
        return Cord(self.x, self.y)

    def __deepcopy__(self, memo):
        return Cord(deepcopy(self.x, memo), deepcopy(self.y, memo))


p1 = Cord(3, 4)
p2 = Cord(1, 2)

print("\nString & Representation:")
print(str(p1))
print(repr(p1))
print(format(p1, ".1f"))

print("\nComparison:")
print(p1 == p2)
print(p1 != p2)
print(p1 > p2)
print(p1 < p2)
print(p1 >= p2)
print(p1 <= p2)

print("\nArithmetic:")
print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1 / p2)
print(p1 // p2)
print(p1 % p2)
print(p1 ** p2)

print("\nReflected:")
print(p2 + p1)
print(p2 * p1)

print("\nIn-place:")
p1 += p2
p1 -= p2
p1 *= p2

print("\nUnary:")
print(-p1)
print(+p1)
print(abs(p1))
print(~Cord(3, 4))

print("\nType Conversion:")
print(int(p1))
print(float(p1))
print(bool(p1))

print("\nCollection-like:")
print(len(p1))
print(p1[0])
print(3 in p1)
p1[0] = 10
del p1[1]

print("\nIteration:")
for i in p1:
    print(i)

print("\nContext Manager:")
with Cord(7, 8) as c:
    print(c)

print("\nCallable:")
p1()

print("\nAttribute Access:")
print(p1.unknown_attr)
del p1.x

print("\nCopying:")
print(copy(p1))
print(deepcopy(p1))

print("\nEnd of tests. Force GC to show __del__:")
import gc
del p1
del p2
gc.collect()

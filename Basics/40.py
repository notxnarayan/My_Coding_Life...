class MagicDemo:
    # Object Creation & Destruction
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self, value):
        print("__init__ called")
        self.value = value

    def __del__(self):
        print("__del__ called")

    # String Representation
    def __str__(self):
        return f"MagicDemo(value={self.value})"

    def __repr__(self):
        return f"MagicDemo({self.value})"

    def __format__(self, format_spec):
        return format(self.value, format_spec)

    # Comparison
    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    # Hashing
    def __hash__(self):
        return hash(self.value)

    # Arithmetic Operators
    def __add__(self, other):
        return MagicDemo(self.value + other.value)

    def __sub__(self, other):
        return MagicDemo(self.value - other.value)

    def __mul__(self, other):
        return MagicDemo(self.value * other.value)

    def __truediv__(self, other):
        return MagicDemo(self.value / other.value)

    def __floordiv__(self, other):
        return MagicDemo(self.value // other.value)

    def __mod__(self, other):
        return MagicDemo(self.value % other.value)

    def __pow__(self, other):
        return MagicDemo(self.value ** other.value)

    # Reflected Arithmetic
    def __radd__(self, other):
        return MagicDemo(other + self.value)

    def __rsub__(self, other):
        return MagicDemo(other - self.value)

    # In-place Arithmetic
    def __iadd__(self, other):
        self.value += other.value
        return self

    def __isub__(self, other):
        self.value -= other.value
        return self

    # Unary Operators
    def __neg__(self):
        return MagicDemo(-self.value)

    def __pos__(self):
        return MagicDemo(+self.value)

    def __abs__(self):
        return MagicDemo(abs(self.value))

    def __invert__(self):
        return MagicDemo(~self.value)

    # Type Conversion
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __bool__(self):
        return bool(self.value)

    # Length & Collection Behavior
    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, index):
        return str(self.value)[index]

    def __setitem__(self, index, val):
        print(f"__setitem__ at {index} to {val} (not really mutable)")

    def __delitem__(self, index):
        print(f"__delitem__ at {index} (not really mutable)")

    def __contains__(self, item):
        return str(item) in str(self.value)

    # Iteration
    def __iter__(self):
        return iter(str(self.value))

    def __next__(self):
        raise StopIteration

    # Context Manager
    def __enter__(self):
        print("__enter__ called")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called")

    # Callable
    def __call__(self, *args, **kwargs):
        print(f"Called with args={args}, kwargs={kwargs}")

    # Attribute Access
    def __getattr__(self, name):
        print(f"__getattr__ for {name}")
        return None

    def __setattr__(self, name, value):
        print(f"__setattr__ for {name} = {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"__delattr__ for {name}")
        super().__delattr__(name)

    # Copy & Pickling (if needed)
    def __copy__(self):
        from copy import copy
        return MagicDemo(self.value)

    def __deepcopy__(self, memo):
        from copy import deepcopy
        return MagicDemo(deepcopy(self.value, memo))


a = MagicDemo(10)
b = MagicDemo(5)

print(a + b)      # __add__
print(a == b)     # __eq__
print(len(a))     # __len__
print('1' in a)   # __contains__

with a as obj:    # __enter__, __exit__
    obj()
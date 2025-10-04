import numpy as np

rng = np.random.default_rng()
b = rng.integers(2,9, size=(2, 4)) # the simplest way to generate random numbers
a = rng.random(3)
print(a)
print(b)
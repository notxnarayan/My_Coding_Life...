import numpy as np

a = np.array([1,2,3,6,7,8])

with np.nditer(a, op_flags=['readwrite']) as it:
   for x in it:
       x[...] = 2 * x
       print(x)
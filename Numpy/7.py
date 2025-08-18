import numpy as np

a = np.arange(99999999).reshape(1,99999999)
b = []
for x in np.nditer(a,flags=['external_loop']):
    print(x, end='|')

import pandas as pd
import numpy as np

np.random.seed(0)
A = np.random.rand(5, 3) * 10
df = pd.DataFrame(A, index=list('abcde'), columns=list('xyz'))
states = [int(i) for i in '2 3 4 5 2'.split()]
df['state'] = states

add = df * df
print(df)
print("================================")
print(add)
print("================================")
print(df>10)
print("================================")
result = df[df['x'] > 5][['x','y']]  # rows where x > 5 --- IGNORE ---
print(result)
print("================================")
result = df[(df['x'] > 5) & (df['x'] < 6)][['x','y']]  # rows where x > 5 and y < 5
print(result)
print("================================")
result = df[(df['x'] > 1) | (df['y'] < 0)][['x','y']]  # rows where x > 5 and y < 5
print(result)
print("================================")

print(df.set_index('state'))
print("================================")
df.reset_index(inplace=True)
print(df)
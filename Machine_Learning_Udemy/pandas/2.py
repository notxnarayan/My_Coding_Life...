import pandas as pd
import numpy as np

np.random.seed(0)
A = np.arange(1, 16).reshape(5, 3)
df = pd.DataFrame(A, index=list('abcde'), columns=list('xyz'))
print(df)
print("===============================")
print(df.loc['a'])
print("===============================")
print(df['x'])  # access column 'x'
print("===============================")
print(df.loc['a', 'x'])  # access element at row 'a' and column 'x'
print("===============================")
print(df.iloc[0, 0])  # access element at first row and first column
print("===============================")
print(df.loc[['a', 'c'], ['x', 'y']])  # access rows 'a' and 'c'
print("===============================")
print(df[df.x > 5])  # rows where x > 5
print("===============================")
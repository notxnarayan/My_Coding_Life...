import numpy as np
import pandas as pd

np.random.seed(0)
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print(df)
print("================================")
print(df.loc['G1'].loc[1])
print("================================")
df.index.names = ['Groups', 'Num']
print(df)
print("================================")
print(df.loc['G2'].loc[2]['B'])
print("================================")
print(df.xs(1,level='Num'))
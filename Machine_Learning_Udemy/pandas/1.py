import pandas as pd
import numpy as np


price = np.array([10, 20, 30, 40, 50])
quantity = np.array(['1', '2', '3', '4', '5'])

series = pd.Series(price, index=quantity)
dataframe= pd.DataFrame({'Quantity': quantity, 'Price': price}, index=quantity)
print(dataframe)
print("================================")
print(dataframe['Price'])
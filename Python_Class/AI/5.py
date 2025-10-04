import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error


data = pd.read_csv('carchal.csv')

# X=data[['Size','Bedroom']]
# y=data['Price']

X=data[['Age']]
y=data['Price']

model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(pd.DataFrame({'Age': [8]}))
print("Predicted value:", y_pred[0])



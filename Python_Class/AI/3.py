import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error


data = pd.read_csv('house_prices.csv')

X=data[['Size','Bedroom']]
y=data['Price']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred= model.predict(X_test)
print("predicted valueeee",y_pred[0])

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=root_mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print("mean absolute error",mae)
print("mean squared error",mse)
print("root mean squared error",rmse)
print("r2 score",r2)
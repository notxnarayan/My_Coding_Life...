import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

diabetes = load_diabetes()
print(diabetes)

X= [[value] for value in diabetes.data[:,2]]
y=diabetes.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2)


model = LinearRegression()
model.fit(X_train,y_train)

y_pred= model.predict(X_test)


# predicted_score = model.predict((np.array([[6]])))
# print(predicted_score)
print("predicted valueeee",y_pred[0])
# print("slope",model.coef_[0])
# print("intercept",model.intercept_)

# plt.scatter(X,y,color="blue")
# plt.plot(X,model.predict(X),color='red')

# plt.scatter(6,predicted_score,color="green")


# plt.xlabel("Hours studied")
# plt.ylabel("score")
# plt.title('linear regression')
# plt.show()
import numpy as np
from sklearn.linear_model import Lasso,Ridge
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


# X =np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y=np.array([0,0,0,0,1,1,1,1,1,1])

# X =np.array([[1000,1],[1500,2],[2000,3],[2500,4],[3000,5],[3500,6],[4000,7],[4500,8],[5000,9],[5500,10]])
X = np.array([
    [1000,1],[1500,2],[2000,3],[2500,4],[3000,5],
    [3500,6],[4000,7],[4500,8],[5000,9],[5500,10]
])
# y=np.array([[50,4],[65,7],[80,10],[95,13],[110,15],[125,17],[140,20],[155,23],[170,25],[195,27]])
y = np.array([
    [50,4],[65,7],[80,10],[95,13],[110,15],
    [125,17],[140,20],[155,23],[170,25],[195,27]
])
poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(X)

lasso_model = Lasso(alpha=100.0,max_iter=10000)
ridge_model=Ridge(alpha=100.0)
lasso_model.fit(X_poly,y)
ridge_model.fit(X_poly,y)

new_student = np.array([[3250,5]])
new_student_poly = poly_features.transform(new_student)
lasso_prediction = lasso_model.predict(new_student_poly)
ridge_prediction = ridge_model.predict(new_student_poly)
print("lassoo prediction",lasso_prediction)
print("ridge prediction",ridge_prediction)
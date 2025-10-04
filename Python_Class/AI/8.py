import numpy as np
from sklearn.linear_model import Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline

# Dataset
X = np.array([
    [1000,1],[1500,2],[2000,3],[2500,4],[3000,5],
    [3500,6],[4000,7],[4500,8],[5000,9],[5500,10]
])
y = np.array([
    [50,4],[65,7],[80,10],[95,13],[110,15],
    [125,17],[140,20],[155,23],[170,25],[195,27]
])

# Ridge pipeline
ridge_pipeline = Pipeline([
    ("poly", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("ridge", Ridge(alpha=10.0))
])

# Lasso pipeline
lasso_pipeline = Pipeline([
    ("poly", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("lasso", Lasso(alpha=0.1, max_iter=10000))
])

ridge_pipeline.fit(X, y)
lasso_pipeline.fit(X, y)

new_student = np.array([[3250, 5]])
ridge_prediction = ridge_pipeline.predict(new_student)
lasso_prediction = lasso_pipeline.predict(new_student)

print("Ridge prediction:", ridge_prediction)
print("Lasso prediction:", lasso_prediction)
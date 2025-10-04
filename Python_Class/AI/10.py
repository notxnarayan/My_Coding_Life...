import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Synthetic data: y = 3x + 2 + noise
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 3 * X[:, 0]**2 + 2 * X[:, 0] + np.random.randn(100) * 2  # Non-linear

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred_lin = lin_reg.predict(X_test)
print("Linear Regression MSE:", mean_squared_error(y_test, y_pred_lin))


from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_reg = LinearRegression()
poly_reg.fit(X_poly_train, y_train)

y_pred_poly = poly_reg.predict(X_poly_test)
print("Polynomial Regression MSE:", mean_squared_error(y_test, y_pred_poly))


from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(max_depth=3, random_state=42)
tree_reg.fit(X_train, y_train)

y_pred_tree = tree_reg.predict(X_test)
print("Decision Tree MSE:", mean_squared_error(y_test, y_pred_tree))


from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(X_train, y_train)

y_pred_forest = forest_reg.predict(X_test)
print("Random Forest MSE:", mean_squared_error(y_test, y_pred_forest))


from sklearn.linear_model import Ridge

ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_poly_train, y_train)

y_pred_ridge = ridge_reg.predict(X_poly_test)
print("Ridge Regression MSE:", mean_squared_error(y_test, y_pred_ridge))


from sklearn.linear_model import Lasso

lasso_reg = Lasso(alpha=0.01, max_iter=10000)
lasso_reg.fit(X_poly_train, y_train)

y_pred_lasso = lasso_reg.predict(X_poly_test)
print("Lasso Regression MSE:", mean_squared_error(y_test, y_pred_lasso))

models = {
    "Linear": y_pred_lin,
    "Polynomial": y_pred_poly,
    "Decision Tree": y_pred_tree,
    "Random Forest": y_pred_forest,
    "Ridge": y_pred_ridge,
    "Lasso": y_pred_lasso
}

for name, preds in models.items():
    mse = mean_squared_error(y_test, preds)
    print(f"{name} MSE: {mse:.2f}")

plt.scatter(X_test, y_test, color="black", label="Test Data")
plt.scatter(X_test, y_pred_lin, label="Linear", alpha=0.6)
plt.scatter(X_test, y_pred_poly, label="Polynomial", alpha=0.6)
plt.scatter(X_test, y_pred_tree, label="Decision Tree", alpha=0.6)
plt.scatter(X_test, y_pred_forest, label="Random Forest", alpha=0.6)
plt.scatter(X_test, y_pred_ridge, label="Ridge", alpha=0.6)
plt.scatter(X_test, y_pred_lasso, label="Lasso", alpha=0.6)

plt.legend()
plt.title("Model Comparison")
plt.show()
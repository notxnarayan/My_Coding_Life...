import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example dataset
# x needs to be 2D for sklearn (reshape from 1D)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1,2,3,4,5])

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Print coefficients
print("Slope (coef):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot results
plt.scatter(X, y, color="blue", label="Data points")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.legend()
plt.show()

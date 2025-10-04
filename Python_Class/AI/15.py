# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
# X = [Weight, Size]
X = np.array([
    [130, 6.0],
    [135, 6.3],
    [140, 6.5],
    [145, 6.8],
    [150, 7.0],
    [155, 7.1],
    [160, 7.3],
    [165, 7.6],
    [170, 7.8],
    [175, 7.9],
    [180, 8.1],
    [185, 8.3],
    [190, 8.4],
    [195, 8.5]
])

# y = Labels (0 = Apple, 1 = Orange)
y = np.array([
    0, 0, 0, 0, 0, 0, 0,   # Apples
    1, 1, 1, 1, 1, 1, 1    # Oranges
])

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

new_point = np.array([[190, 6]])
predicted_class = knn.predict(new_point)[0]
neighbors = knn.kneighbors(new_point, return_distance=True)

distances, indices = neighbors
print("Nearest neighbors indices:", indices)
print("Nearest neighbors distances:", distances)
print("New Prediction: ", "Apple" if predicted_class == 0 else "Orange")
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', s=100, label='Training points')
plt.scatter(X[indices[0],0], X[indices[0],1], s=200, facecolors='none', edgecolors='black', label='Nearest neighbors')
plt.scatter(new_point[:,0], new_point[:,1], c='green', s=150, marker='*', label=f'New point (Class {predicted_class})')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title(f'KNN Visualization (K={k})')
plt.legend()
plt.show()


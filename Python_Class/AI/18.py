import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Sample 3-class data
X = np.array([
    [1, 2], [2, 3], [3, 1],       # Class 0
    [6, 5], [7, 7], [8, 6],       # Class 1
    [3, 7], [4, 8], [5, 9]        # Class 2
])
y = np.array([0,0,0, 1,1,1, 2,2,2])

# Train linear SVM (multi-class handled automatically)
model = SVC(kernel='linear')
model.fit(X, y)

# Plot decision boundaries
xx, yy = np.meshgrid(np.linspace(0,9,300), np.linspace(0,10,300))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
plt.scatter(X[y==0,0], X[y==0,1], color='red', label='Class 0')
plt.scatter(X[y==1,0], X[y==1,1], color='blue', label='Class 1')
plt.scatter(X[y==2,0], X[y==2,1], color='green', label='Class 2')
plt.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1],
            s=100, facecolors='none', edgecolors='k', label='Support Vectors')
plt.title("3-Class Linear SVM in 2D")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.show()
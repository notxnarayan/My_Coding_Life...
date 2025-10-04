import numpy as np

# -------------------------
# Step 1: Sample Data (Age, Income in thousands)
# -------------------------
X = np.array([
    [20, 25],
    [22, 27],
    [25, 90],
    [45, 95],
    [50, 100],
    [35, 40]
])

# Number of clusters
K = 3

# -------------------------
# Step 2: Initialize centroids (randomly pick K points from data)
# -------------------------
np.random.seed(42)
initial_centroids = X[np.random.choice(X.shape[0], K, replace=False)]
centroids = initial_centroids.copy()
print("Initial Centroids:\n", centroids)

# -------------------------
# Step 3: K-Means Algorithm
# -------------------------
for iteration in range(5):  # run few iterations manually
    # Assign each point to nearest centroid
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)

    # Recalculate centroids
    new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])

    print(f"\nIteration {iteration+1}")
    for k in range(K):
        print(f" Cluster {k+1} points:\n", X[labels == k])
        print(f" New Centroid {k+1}:", new_centroids[k])

    # Update centroids
    centroids = new_centroids
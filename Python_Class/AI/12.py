import numpy as np
import matplotlib.pyplot as plt

# -------------------------
X = np.array([
    [15, 39],
    [16, 81],
    [17, 6],
    [18, 77],
    [19, 40]
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

# record centroid positions so we can visualize them later
centroids_history = [centroids.copy()]

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

    # record and update
    centroids_history.append(new_centroids.copy())
    centroids = new_centroids

# Convert history to array with shape (steps, K, 2)
centroids_history = np.array(centroids_history)

# -------------------------
# Visualizations
# 1) Centroid trajectories overlaid on data
# 2) Centroid coordinates (feature1 & feature2) vs iteration (two subplots)
# 3) Centroid movement magnitude per iteration
# -------------------------

# 1) Trajectories
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c='lightgray', s=80, edgecolors='k', label='Data points')
colors = ['r', 'g', 'b', 'c', 'm', 'y']
for k in range(K):
    traj = centroids_history[:, k, :]
    plt.plot(traj[:, 0], traj[:, 1], '-o', color=colors[k % len(colors)], label=f'Centroid {k+1}')
    plt.scatter(traj[0, 0], traj[0, 1], marker='X', s=120, color=colors[k % len(colors)], edgecolors='k')
    plt.scatter(traj[-1, 0], traj[-1, 1], marker='P', s=120, color=colors[k % len(colors)], edgecolors='k')
plt.title('Centroid trajectories over data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

# 2) Coordinates vs iteration
steps = centroids_history.shape[0]
iters = np.arange(steps)
fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=False)
for k in range(K):
    axes[0].plot(iters, centroids_history[:, k, 0], '-o', color=colors[k % len(colors)], label=f'Centroid {k+1}')
    axes[1].plot(iters, centroids_history[:, k, 1], '-o', color=colors[k % len(colors)], label=f'Centroid {k+1}')
axes[0].set_title('Feature 1 (x) of centroids vs iteration')
axes[0].set_xlabel('Iteration')
axes[0].set_ylabel('Feature 1')
axes[1].set_title('Feature 2 (y) of centroids vs iteration')
axes[1].set_xlabel('Iteration')
axes[1].set_ylabel('Feature 2')
axes[0].legend()
axes[1].legend()
axes[0].grid(True)
axes[1].grid(True)
plt.tight_layout()
plt.show()

# 3) Movement magnitude per iteration
displacements = np.linalg.norm(centroids_history[1:] - centroids_history[:-1], axis=2)  # shape (steps-1, K)
plt.figure(figsize=(8, 5))
for k in range(K):
    plt.plot(np.arange(1, steps), displacements[:, k], '-o', color=colors[k % len(colors)], label=f'Centroid {k+1}')
plt.title('Centroid movement magnitude per iteration')
plt.xlabel('Iteration')
plt.ylabel('Movement (L2 distance)')
plt.legend()
plt.grid(True)
plt.show()

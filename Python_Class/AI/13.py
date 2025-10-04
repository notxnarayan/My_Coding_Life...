import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
data = {
    'Annual Income (k$)': [15, 16, 17, 18, 19, 30, 35, 70, 85, 90],
    'Spending Score (1-100)': [39, 81, 6, 77, 40, 50, 45, 20, 15, 90]
}
df = pd.DataFrame(data)

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Elbow method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  # inertia_ = WCSS

# Plot the elbow graph
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal K')
plt.show()
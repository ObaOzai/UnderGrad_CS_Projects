"""

K-Means Clustering Overview

K-Means Clustering is an unsupervised machine learning algorithm used to partition a dataset into 
K clusters based on feature similarity.

It’s commonly used in data mining, pattern recognition, market segmentation, and image compression.
The goal is to minimize the sum of the squared distances between each point and the centroid of its assigned cluster.

Concept

1. Choose K (the number of clusters). 

2. Initialize centroids: Randomly select K points as the initial centroids.

3. Assign points to the nearest centroid: Each data point is assigned to the cluster whose centroid is closest.

4. Update centroids: Calculate the new centroid of each cluster based on the points assigned to it.

5. Repeat steps 3 and 4 until the centroids do not change significantly (convergence).

Objective Function: The goal is to minimize the following cost function:

<ommited>

Where:

K is the number of clusters.

Ci is the set of points in cluster i.

μi is the centroid of cluster i.

Let’s implement K-Means Clustering using Python’s scikit-learn library. 
We’ll also visualize the results using matplotlib

Explanation of the Code

Generating Synthetic Data:
We use make_blobs from scikit-learn to generate a dataset with 4 clusters.

K-Means Clustering:
We initialize the KMeans object with: n_clusters=4: Number of clusters.

init='k-means++': A smart way of initializing the centroids to speed up convergence.

n_init=10: Number of times the algorithm will run with different centroid seeds.
max_iter=300: Maximum number of iterations for a single run.

Fitting the Model:
We fit the model to our data using kmeans.fit_predict(X).

Measuring Performance:
We use time.time() to measure how long the clustering process takes.

Plotting the Clusters:
We visualize the clusters and centroids using matplotlib.

Output

K-Means clustering completed in 0.0420 seconds

Cluster centers:
[[ 1.9895  0.7885]
 [-1.4175  3.2741]
 [ 0.9392  4.4081]
 [-1.7537  0.8657]]

"""

# K-Means Clustering Algorithm using scikit-learn
# Astro Pema Software (c)
# Oba Ozai - JD Correa

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import time

# Generate synthetic data
np.random.seed(0)
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Start timer
start_time = time.time()

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# End timer
end_time = time.time()

# Print the results
print(f"K-Means clustering completed in {end_time - start_time:.4f} seconds")
print(f"Cluster centers:\n{kmeans.cluster_centers_}")

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

# EOF






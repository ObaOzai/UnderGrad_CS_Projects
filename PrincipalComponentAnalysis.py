"""

Principal Component Analysis (PCA) Overview

PCA is a dimensionality reduction technique that transforms data into a lower-dimensional 
space while preserving as much variance as possible.

It is commonly used for data compression, noise reduction, feature extraction, and visualization.
PCA identifies the principal components, which are the directions of maximum variance in the dataset.

Concept
Standardize the Data: Subtract the mean and divide by the standard deviation for each feature.
Covariance Matrix: Calculate the covariance matrix to understand how features vary with respect to each other.
Eigenvalues and Eigenvectors: Compute the eigenvalues and eigenvectors of the covariance matrix.
Select Principal Components: Sort the eigenvalues in descending order and choose the top
k eigenvectors as the principal components.
Transform Data: Project the original data onto the new principal component space.

Explanation of the Code

Loading the Dataset:
We load the Iris dataset, which contains 150 samples, each with 4 features (sepal length, sepal width, petal length, and petal width).

Standardizing the Features:
We use StandardScaler to standardize the features so that they have a mean of 0 and a standard deviation of 1.

Applying PCA:
We use PCA(n_components=2) to reduce the data to 2 dimensions.
The explained_variance_ratio_ tells us how much variance is captured by each principal component.

Plotting the Results:
We visualize the data in the new 2-dimensional space using the two principal components.

Output
Explained variance by each component: [0.7296 0.2285]
This indicates that the first principal component explains about 73% of 
the variance, and the second explains about 23%.

You’ll also see a scatter plot showing the Iris dataset reduced to 2 
dimensions, with different colors representing the three classes of flowers.

"""

# Principal Component Analysis (PCA) Example
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target
target_names = data.target_names

# Step 1: Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
X_pca = pca.fit_transform(X_scaled)

print("Explained variance by each component:", pca.explained_variance_ratio_)

# Step 3: Visualize the PCA results
plt.figure(figsize=(10, 6))
colors = ['r', 'g', 'b']
for i, target in enumerate(np.unique(y)):
    plt.scatter(X_pca[y == target, 0], X_pca[y == target, 1], 
                label=target_names[target], color=colors[i])
    
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.show()

# EOF


import random

import numpy as np


def k_means(data, k, max_iterations=100):
    # Randomly initialize k centroids
    centroids = random.sample(list(data), k)

    for iteration in range(max_iterations):
        # Assign data points to the nearest centroid
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [np.linalg.norm(point - centroid)
                         for centroid in centroids]
            closest_cluster = np.argmin(distances)
            clusters[closest_cluster].append(point)

        # Update centroids based on the mean of data points in each cluster
        new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]

        # Check for convergence
        if np.allclose(new_centroids, centroids):
            break

        centroids = new_centroids

    return clusters, centroids


# Example usage
if __name__ == "__main__":
    # Generate some random data points for demonstration
    np.random.seed(42)
    data = np.random.rand(100, 2)

    k = 3  # Number of clusters
    clusters, centroids = k_means(data, k)

    print("Final centroids:")
    print(centroids)

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)

labels = kmeans.labels_
dcolor = {1:"red", 0:"green"}
for idx, val in enumerate(X):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', linewidths=3)
plt.show()
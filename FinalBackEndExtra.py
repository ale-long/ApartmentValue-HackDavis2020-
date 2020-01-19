from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

input_file = pd.read_csv('C:\\Users\\jalas\\OneDrive\\Desktop\\hackdavis\\listingsfinal.csv')
apart_arr = input_file.to_numpy()

fig = plt.figure('Square Feet vs Price')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  if apart_arr[idx][2][0].isdigit() == True:
      sqft = int(apart_arr[idx][2][0:4])
      num_arr.append([price, sqft])    

#dummy points to demonstrate bad region
num_arr.append([2130, 100])
num_arr.append([2250, 75])

test = []
range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(num_arr)
    silhouette_avg = silhouette_score(num_arr, cluster_labels)
    test.append([n_clusters, silhouette_avg])
print(test)


themax = 0
clustersneeded = 0
for idx, val in enumerate(test):
        if val[1] > themax:
            themax = val[1]
            clustersneeded = val[0]
print(clustersneeded)
print(themax)

kmeans = KMeans(n_clusters=clustersneeded, random_state=0).fit(num_arr)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
print(centers)

colors = []
for idx, val in enumerate(centers):
    clustervalue = float(val[0]) / float(val[1])
    print(clustervalue)
    if clustervalue < (1):
        colors.append([idx, 1])
    elif (1) <= clustervalue <= (2):
        colors.append([idx, 0])
    elif clustervalue > (2):
        colors.append([idx, -1])

dcolor = {-1:"red", 0:"yellow", 1:"green"}
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[colors[labels[idx]][1]])
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.title("Square Feet vs Prices")
plt.xlabel("Prices per Month")
plt.ylabel("Square Feet")

plt.show(fig)
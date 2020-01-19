from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

input_file = pd.read_csv('C:\\Users\\jalas\\OneDrive\\Desktop\\hackdavis\\listings2.1.csv')
apart_arr = input_file.to_numpy()

#sqft graph
plt.figure('Sqft vs Price')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  if apart_arr[idx][3][0].isdigit() == True:
      sqft = int(apart_arr[idx][3][0:4])
      num_arr.append([price, sqft])    

test = []
range_n_clusters = [2, 3, 4, 5, 6]
for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(num_arr)
    silhouette_avg = silhouette_score(num_arr, cluster_labels)
    test.append([n_clusters, silhouette_avg])

    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)
print(test)

max = 0
clustersneeded = 0
for range_n_clusters, val in enumerate(test):
    for x in range(1):
     if test[range_n_clusters][x] > max:
         max = test[range_n_clusters][x] 
         print(max)     

#kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
#labels = kmeans.labels_
#dcolor = {0:"red", 1:"orange", 2:"yellow"}
#for idx, val in enumerate(num_arr):
#    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
#centers = kmeans.cluster_centers_
#plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
#plt.title("Sqft vs Prices")
#plt.xlabel("Prices per Month")
#plt.ylabel("Sqft")
#
#plt.show()
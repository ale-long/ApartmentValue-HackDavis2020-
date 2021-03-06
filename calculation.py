from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

input_file = pd.read_csv('C:\\Users\\jalas\\OneDrive\\Desktop\\hackdavis\\listings2.csv')
#print(input_file.head())
apart_arr = input_file.to_numpy()
#print(apart_arr)
#print(apart_arr[1][4])

num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  bed = int(apart_arr[idx][4][0])
  num_arr.append([price, bed])
#print(num_arr)
kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
#print(kmeans.labels_)
#print(kmeans.cluster_centers_)
labels = kmeans.labels_
dcolor = {0:"red", 1:"orange", 2:"yellow"}
plt.figure('Beds vs Prices')
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.show()
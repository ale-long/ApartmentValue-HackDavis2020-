from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

input_file = pd.read_csv('C:\\Users\\jalas\\OneDrive\\Desktop\\hackdavis\\listings2.1.csv')
apart_arr = input_file.to_numpy()

#bed graph
plt.figure('Beds vs Prices')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  bed = int(apart_arr[idx][4][0])
  num_arr.append([price, bed])
kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
labels = kmeans.labels_
dcolor = {0:"red", 1:"orange", 2:"yellow"}
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.title("Beds vs Prices")
plt.xlabel("Prices per Month")
plt.ylabel("Number of Beds")

#bath graph
plt.figure('Baths vs Prices')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  bath = int(apart_arr[idx][5][0])
  num_arr.append([price, bath])
kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
labels = kmeans.labels_
dcolor = {0:"red", 1:"orange", 2:"yellow"}
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.title("Baths vs Prices")
plt.xlabel("Prices per Month")
plt.ylabel("Number of Baths")

#distance graph
plt.figure('Distance vs Price')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  distance = float(apart_arr[idx][6][0:3])
  num_arr.append([price, distance]) 
kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
labels = kmeans.labels_
dcolor = {0:"red", 1:"orange", 2:"yellow"}
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.title("Distances vs Prices")
plt.xlabel("Prices per Month")
plt.ylabel("Distance in Miles")

#rating graph
plt.figure('Rating vs Price')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  if apart_arr[idx][7][0].isdigit() == True:
      rating = float(apart_arr[idx][7][0:3])
      num_arr.append([price, rating])    
kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
labels = kmeans.labels_
dcolor = {0:"red", 1:"orange", 2:"yellow"}
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.title("Ratings vs Prices")
plt.xlabel("Prices per Month")
plt.ylabel("Ratings")

#sqft graph
plt.figure('Sqft vs Price')
num_arr = []
for idx, val in enumerate(apart_arr):
  price = int(apart_arr[idx][0][1:5])
  if apart_arr[idx][3][0].isdigit() == True:
      sqft = int(apart_arr[idx][3][0:4])
      num_arr.append([price, sqft])    
kmeans = KMeans(n_clusters=3, random_state=0).fit(num_arr)
labels = kmeans.labels_
dcolor = {0:"red", 1:"orange", 2:"yellow"}
for idx, val in enumerate(num_arr):
    plt.scatter(val[0], val[1], color=dcolor[labels[idx]])
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x')
plt.title("Sqft vs Prices")
plt.xlabel("Prices per Month")
plt.ylabel("Sqft")

#now we put weights on each apartment aspect
#price + distance + sqft + bed

price_weight = input("Enter a weight for price(decimal between 0 and 1): ")
distance_weight = input("Enter a weight for distance(decimal between 0 and 1): ")
sqft_weight = input("Enter a weight for sqft(decimal between 0 and 1): ") 
#bed_weight = input("Enter a weight for ")


plt.show()
import pandas as pd
import numpy as np
import random
import math
from sklearn.utils import shuffle


K = 3	# used for the iris-test.dat data set
# K = 10	# used for the image clustering data set


# Image Clustering
# Samuel Geremew

# Using K-Means algorithm this program will take in a data set of images of 
# hand-written digits and classify them.

# import_data():	Takes in a file and returns a DataFrame of records
# Parameters:	file: file of data points/records
# Returns:	data: data set of points (DataFrame)
def import_data(file):
	# Since features do not have labels we set header=None and sep=' ' so that 
	# instead we store the index as the attribute names
	data = pd.read_csv(file,sep=' ',header=None)
	return data

# find_centroids():	randomly selects centroids from the give data set
# Parameters:	data: data set of points (DataFrame)
# Returns:	centroids: array of centroids (DataFrame)
def find_centroids(data):
	data = shuffle(data)
	centroids = data.iloc[:K]
	return centroids

def best_centroids(runs,data):
	
	clist = []
	scores = []

	for i in range(runs):
		c = find_centroids(data)
		clist.append(c)

	dist = 0
	for c in clist:
		dist += euclidean_dist(c.iloc[0],c.iloc[1])
		dist += euclidean_dist(c.iloc[1],c.iloc[2])
		dist += euclidean_dist(c.iloc[2],c.iloc[0])
		scores.append(dist)

	index = np.argmax(scores)

	print(f'Best Centroids:\n{clist[index]}')
	return clist[index]


# euclidean_dist():	calculates the euclidean distance between two points
# Parameters:	p and q: are both data points (Series)
# Returns:	dist: is the euclidean distance calculated (float)
def euclidean_dist(p,q):
	total = 0

	for i in range(len(p)):
		num = p[i] - q[i]
		num = num*num
		total = total + num
	dist = math.sqrt(total)
	return dist

# pairwise_minimums():	finds the minimum distance of a point to a set of points
# Parameters:	data: data set of points (DataFrame)
# 				centroids: array of centroids (DataFrame)
# Returns:	labels: the centroids that were closest to data points
def pairwise_minimums(data, centroids):

	labels = []
	# loops through the data points
	for i in range(len(data)):
		min_dist = euclidean_dist(data.iloc[i],centroids.iloc[0])
		label = 1
		# loops through the centroids
		for j in range(len(centroids)):
			dist = euclidean_dist(data.iloc[i],centroids.iloc[j])
			# determines the minimum distance
			if(dist < min_dist):
				min_dist = dist
				label = j+1
		labels.append(label)

	return labels

def mean_of_points(data,labels):

	# arr = data.to_numpy()
	# # for i in range(len(labels)):
	# for i in range(K):
	# 	centroids = np.array(arr[labels == (i+1)].mean(0))
	# # centroids = np.array([data[labels == (i+1)].mean(0) \
 # #                            for i in range(K)])
 # clusters(data, K)
	# centers = best_centroids(3,data)
	# labels = pairwise_minimums(data, centers)
	# mean_of_points(data,labels)
	# print(labels)
	data = data.to_numpy()

	new_centers = []
	labelx = []

	for i in range(K):
		for j in range(len(labels)):
			if labels[j] == (i+1):
				labelx.append(data[j])
				# print(f'Index: {j}, Label: {labels[j]}')
		# print("NEXT---------")
			
		arr = np.asarray(labelx)		
		# print(arr)
		# print(arr.mean(0))
		mean = arr.mean(0)
		# np.append(arr=new_centers,values=mean,axis=0)

		new_centers.append(mean)
		# print(f'Iteration {i}: {new_centers}')
	# print(f'New Centers: {new_centers}')
	recomputed = pd.DataFrame(data=new_centers)
	print(f'Recomputed:\n{recomputed}')
	# print(type(recomputed))
	# print(recomputed)
	return recomputed

# clusters():	uses the K-Means clustering algorithm to identify clusters in 
# 				the data set
# Parameters:	data: data set of points (DataFrame)
# 				k: number of clusters (int)
# Returns:	array of labels (numpy.ndarray) and an array of centroids 
# 			(numpy.ndarray)
def clusters(data, k):

	# 2a. Assign labels based on closest center
	centroids = best_centroids(3,data)

	while True:
		labels = pairwise_minimums(data, centroids)

		# 2b. Find new centers from means of points
		new_centers = mean_of_points(data, labels)

		# 2c. Check for convergence
		if (centroids.equals(new_centers)):
		    break
		centroids = new_centers
	# return centroids, labels
	return labels


def main():
	file = "../iris-test.dat"
	data = import_data(file)

	# print(clusters(data,K))


	labels = clusters(data,K)

	

main()



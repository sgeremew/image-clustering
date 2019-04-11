import pandas as pd
import numpy as np
import random
import math
from sklearn.utils import shuffle


K = 3	# used for the iris-test.dat data set
# K = 10	# used for the image clustering data set


# Image Clustering
# Samuel Geremew

# Using K-Means algorithm this program will take in a data set of images of hand-
# written digits and classify them.

# import_data():	Takes in a file and returns a DataFrame of records
# Parameters:	file: file of data points/records
# Returns:	data: data set of points (DataFrame)
def import_data(file):
	# Since features do not have labels we set header=None so that instead we store 
	# the index as the attribute names
	data = pd.read_csv(file,sep=' ',header=None)
	return data

# find_centroids():	randomly selects centroids from the give data set
# Parameters:	data: data set of points (DataFrame)
# Returns:	centroids: array of centroids (DataFrame)
def find_centroids(data):
	data = shuffle(data)
	centroids = data.iloc[:K]
	return centroids


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
# Returns:	minimum: the centroid that was closest to data[i,:] (numpy.ndarray)
def pairwise_minimums(data, centroids):

	# point = data.iloc[0]
	# min_dist = centroids.iloc[0] - point
	return None

# clusters():	uses the K-Means clustering algorithm to identify clusters in 
#				the data set
# Parameters:	data: data set of points (DataFrame)
# 				k: number of clusters (int)
# Returns:	array of labels (numpy.ndarray) and an array of centroids 
# 			(numpy.ndarray)
def clusters(data, k):
	return None


def main():
	file = "../iris-test.dat"
	data = import_data(file)

	# print(find_centroids(data))
	print(data)
	print(type(data))
	print(euclidean_dist(data.iloc[0],data.iloc[1]))
	# a = data.iloc[0][0]
	# print(a)
	# print(a.iloc[0,1])

main()



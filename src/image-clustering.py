import pandas as pd
import numpy as np
import random
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
	data = pd.read_csv(file,header=None)
	return data

# find_centroids():	randomly selects centroids from the give data set
# Parameters:	data: data set of points (DataFrame)
# Returns:	centroids: array of centroids (DataFrame)
def find_centroids(data):
	# range_ = np.random.RandomState(seed)
	data = shuffle(data)
	# i = data.iloc[:K]
	centroids = data.iloc[:K]
	return centroids

def euclidean_dist(p,q):



# pairwise_minimums():	finds the minimum distance of a point to a set of points
# Parameters:	data: data set of points (DataFrame)
# 				centroids: array of centroids (DataFrame)
# Returns:	minimum: the centroid that was closest to data[i,:] (numpy.ndarray)
def pairwise_minimums(data, centroids):

	point = data.iloc[0]
	# min_dist = centroids.iloc[0] - point

# # clusters():	uses the K-Means clustering algorithm to identify clusters in 
# #				the data set
# # Parameters:	data: data set of points (DataFrame)
# # 				k: number of clusters (int)
# # Returns:	array of labels (numpy.ndarray) and an array of centroids 
# # 			(numpy.ndarray)
# def clusters(data, k):



def main():
	file = "../iris-test.dat"
	data = import_data(file)

	print(find_centroids(data))
	print(data)


main()



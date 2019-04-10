import pandas as pd
import numpy as np
import random

K = 3	# used for the iris-test.dat dataset
# K = 10	# used for the image clustering dataset


# Image Clustering
# Samuel Geremew

# Using K-Means algorithm this program will take in a dataset of images of hand-
# written digits and classify them.

# import_data():	Takes in a file and returns a DataFrame of records
# Parameters:	file: file of data points/records
# Returns:	data: dataset of points (DataFrame)
def import_data(file):
	# Since features do not have labels we set header=None so that instead we store 
	# the index as the attribute names
	data = pd.read_csv(file,header=None)
	return data

# seed: random number seed (int)
# Parameters:	data: dataset of points (DataFrame)
# 				seed: for our random number generator
# Returns:	centroids: array of centroids (numpy.ndarray)
def find_centroids(data, seed=3):
	range_ = np.random.RandomState(seed)
    i = range_.permutation(data.shape[0])[:K]
    centroids = X[i]
    return centroids


# # pairwise_minimums():	finds the minimum distance of a point to a set of points
# # Parameters:	data: dataset of points (DataFrame)
# # 				centroids: array of centroids (numpy.ndarray)
# # Returns:	minimum: the centroid that was closest to data[i,:] (numpy.ndarray)
# def pairwise_minimums(data, centroids):


# # clusters():	uses the K-Means clustering algorithm to identify clusters in 
# #				the dataset
# # Parameters:	data: dataset of points (DataFrame)
# # 				k: number of clusters (int)
# # Returns:	array of labels (numpy.ndarray) and an array of centroids 
# # 			(numpy.ndarray)
# def clusters(data, k):



def main():
	file = "../iris-test.dat"
	data = import_data(file)

	# print(data)

main()



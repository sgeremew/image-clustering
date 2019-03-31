# Image Clustering
# Samuel Geremew

# Using K-Means algorithm this program will take in a dataset of images of hand-
# written digits and classify them.


# seed: random number seed (int)
# Parameters:	data: dataset of points (DataFrame)
# 				seed: for our random number generator
# Returns:	centroids: array of centroids (numpy.ndarray)
def find_centroids(data, seed=3):


# pairwise_minimums():	finds the minimum distance of a point to a set of points
# Parameters:	data: dataset of points (DataFrame)
# 				centroids: array of centroids (numpy.ndarray)
# Returns:	minimum: the centroid that was closest to data[i,:] (numpy.ndarray)
def pairwise_minimums(data, centroids):


# clusters():	uses the K-Means clustering algorithm to identify clusters in 
#				the dataset
# Parameters:	data: dataset of points (DataFrame)
# 				k: number of clusters (int)
# Returns:	array of labels (numpy.ndarray) and an array of centroids 
# 			(numpy.ndarray)
def clusters(data, k):



# image-clustering

Overview and Goals:
-------------------
The objectives are the following: 

* Implement the K-Means Algorithm
* Deal with Image data (processed and stored in vector format)
* Think about Best Metrics for Evaluating Clustering Solutions

-----------------------------------------------------------------------------------------------------------------------------

Detailed Description:
---------------------
* There are 2 leaderbooard submissions and this is the main assignment. 
* Iris files have an easier dataset where K-Means can be tested quickly.  

Implement the K-Means algorithm. Libraries used are only for pre-processing.

Input Data (provided as new_test.txt) consists of 10,000 images of handwritten digits (0-9). The images were scanned and 
scaled into 28x28 pixels. For every digit, each pixel can be represented as an integer in the range [0, 255] where 0 
corresponds to the pixel being completely white, and 255 corresponds to the pixel being completely black. This gives us a 
28x28 matrix of integers for each digit. We can then flatten each matrix into a 1x784 vector. There are no provided labels.

Format of the input data: Each row is a record (image), which contains 784 comma-delimited integers.

For Evaluation Purposes (Leaderboard Ranking), we will use the V-measure in the sci-kit learn library that is considered an 
external index metric to evaluate clustering. Essentially the task is to assign each of the instances in the input data to K 
clusters identified from 1 to K. 

For the leaderboard evaluation set K to 10. Submit the best results. The leaderboard will report the V-measure on 50% of 
sampled dataset. 

Note: format.txt shows an example file containing 10,000 rows with random class assignments from 1 to 10.  

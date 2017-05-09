#! /usr/bin/python

import pandas as pd
import numpy as np
from sklearn import cross_validation
from sklearn import tree
from skfeature.function.information_theoretical_based import JMI
import math

def discr():

	#	Reading the input data (Please ensure to change location and the file name when you edit & execute this script)

	data = pd.read_csv("/home/jarvis/Downloads/Tic_Toc.csv")
	csv = data.as_matrix()

	#	Features
	X = csv[:,:-1]
	
	# Labels
	Y = csv[:,-1]

	n, m = X.shape
	X_bins = []
	X_bins_1 = []
	X_bins_11 = []
	names= (data.columns.values)

	#	Discretizing function

	for i in xrange(m):
        	l1 = np.unique(X[:,i])
        	if len(l1)<=2:
                	X_bins_11.append(X[:,i])
        	else:
                	if len(l1)<=25:
                        	n1 = len(l1)
                	else:
                        	n1 = math.ceil(math.sqrt(n))
                	n_bins = np.linspace(0, np.amax(X[:,i]), n)
                	X_bins_1 = np.digitize(X[:,i], n_bins)
                	X_bins_11.append(X_bins_1)
	X_bins = np.transpose(X_bins_11)
	X1 = np.column_stack((X_bins,Y))

	#	Writing to a csv file

	out = open("discretize.csv","w")
	for name in names:
		out.write("%s"%name)
		out.write('\t')
	out.write('\n')
	for row in X1:
		for i in row:		
			out.write("%d"%i)
			out.write('\t')
		out.write('\n')
	out.close

if __name__=="__main__":
	discr()
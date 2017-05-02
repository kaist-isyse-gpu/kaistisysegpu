import numpy as np
import matplotlib.pyplot as plt
import csv

%matplotlib inline

X = []
Y = []

f = open('X.csv', 'r')
csvReader = csv.reader(f)

for row in csvReader:
    X.append(row)
    
f = open('Y.csv', 'r')
csvReader = csv.reader(f)

for row in csvReader:
    Y.append(row)
    
f.close()

X = np.asarray(X, dtype = 'float64')
Y = np.asarray(Y, dtype = 'float64')
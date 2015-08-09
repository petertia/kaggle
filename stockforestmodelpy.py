import csv as csv
import numpy as np
import scipy

from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

# create an array from the csv file
day1_data = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Battlefin/data/1.csv','rt'))
header = next(day1_data)

data1 = []

for row in day1_data:
    data1.append(row)

data1 = np.array(data1)

# create an array from the csv file
day2_data = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Battlefin/data/2.csv','rt'))
header = next(day2_data)

data2 = []

for row in day2_data:
    data2.append(row)

data2 = np.array(data2)

# create an array from the csv file
train_data = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Battlefin/trainLabels.csv','rt'))
header = next(train_data)

train_array = []

for row in train_data:
    train_array.append(row)

train_array = np.array(train_array)

# create the random forest object which will include all the parameters
# for the fit
Forest = RandomForestClassifier(n_estimators = 100)

Forest = Forest.fit(data1[0::,1:198],train_array[0, 1])

Output = Forest.predict(data2[1::,1:198])

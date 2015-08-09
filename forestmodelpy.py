import csv as csv
import numpy as np
import scipy

from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

train_data = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Titanic/train_forest.csv','rt'))
header = next(train_data)
data = []
data2 = []

for row in train_data:
	data.append(row)
	
data = np.array(data)


# create an array from the csv file
test_data = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Titanic/test3.csv','rt'))
header = next(test_data)

for row in test_data:
	data2.append(row)
	
data2 = np.array(data2)


# create the random forest object which will include all the parameters
# for the fit
Forest = RandomForestClassifier(n_estimators = 100)

# Fit the training data to the training output and create the
# decision trees
# fit(x,y) builds a forest where
# x is the training input samples and y is the target values
Forest = Forest.fit(data[0::,2::],data[0::,1])

# Take the same decision trees and run on the test data
Output = Forest.predict(data2[0::,1::])


# Create each column with the desired data
ForestOutputCol1 = data2[0::,0]
ForestOutputCol2 = Output

# Combine the columns to create a new array
ForestOutput = np.vstack((ForestOutputCol1,ForestOutputCol2)).T


with open('C:/Users/Peter/Documents/Kaggle/Titanic/forestmodel.csv', 'w', newline='') as csvWriterfile:
                open_file_object = csv.writer(csvWriterfile, dialect='excel')
                open_file_object.writerow(["PassengerId", "Survived"])

                for values in ForestOutput:
                        open_file_object.writerow(values)


import csv as csv
import numpy as np

csv_file_object = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Titanic/train.csv','rt'))
header = next(csv_file_object)
data = []

for row in csv_file_object:
	data.append(row)
	
data = np.array(data)

# Creating bins for gender, class, fare


fare_ceiling = 40
data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling-1.0
fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size
number_of_classes = 3
number_of_price_brackets = int(number_of_price_brackets)

#Define survival table
survival_table = np.zeros([2, number_of_classes, number_of_price_brackets])

for i in range(number_of_classes):
        for j in range(number_of_price_brackets):
                # sets the data for each range to a vector and finds the mean
                # then enters the data into the survival table and repeats the for loop
                women_only_stats = (data[(data[0::,4] == "female")  \
                                         # which is a female
                                &(data[0::,2].astype(np.float)== i+1)    \
                                         # and was ith class
                                &(data[0:,9].astype(np.float) >= j*fare_bracket_size)    \
                                         #and was greater than this bin
                                &(data[0:,9].astype(np.float) < (j+1)*fare_bracket_size), 1]) \
                                #and less than the next bin in the 1st col

                
                men_only_stats = (data[(data[0::,4] != "female") \
                                       # which is a male
                                &(data[0::,2].astype(np.float) == i+1)  \
                                       # and was ith class
                                &(data[0:,9].astype(np.float) >= j*fare_bracket_size)  \
                                       #and was greater than this bin
                                &(data[0:,9].astype(np.float) < (j+1) * fare_bracket_size), 1])   \
                                #and less than the next bin in the 1st col
                if len(women_only_stats) > 0:
                
                        survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))      #women stats

                if len(men_only_stats) > 0:
                        survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))      #men stats

survival_table[survival_table != survival_table] = 0

survival_table[survival_table < 0.5] = 0
survival_table[survival_table >= 0.5] = 1

with open('C:/Users/Peter/Documents/Kaggle/Titanic/test.csv', newline='') as csvTestfile:
        test_file_object = csv.reader(csvTestfile, dialect='excel')
        header = next(test_file_object)
        with open('C:/Users/Peter/Documents/Kaggle/Titanic/genderclassmodelpy.csv', 'w', newline='') as csvWriterfile:
                open_file_object = csv.writer(csvWriterfile, dialect='excel')
                open_file_object.writerow(["PassengerId", "Survived"])


                for row in test_file_object: #loop through each passenger in the test file
                        for j in range(number_of_price_brackets): #for each passenger do

                                try: #try to make the numbers a float
                                        row[8] = float(row[8])
                                except: #if there's no number set the bin according to class
                                        bin_fare = 3-float(row[1])
                                        break
                                if row[8] > fare_ceiling:
                                        bin_fare = number_of_price_brackets-1
                                        break
                                if row[8] >= j*fare_bracket_size and row[8] < (j+1)*fare_bracket_size:
                                                bin_fare = j
                                                break
                        if row[3] == 'female':
                                row.insert(1, int(survival_table[0,float(row[1])-1, bin_fare]))
                                open_file_object.writerow((row[0],row[1]))
                        else:
                                row.insert(1, int(survival_table[1,float(row[1])-1,bin_fare]))
                                open_file_object.writerow((row[0],row[1]))



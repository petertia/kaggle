import numpy
import csv as csv
import numpy as np
csv_file_object = csv.reader(open('C:/Users/Peter/Documents/Kaggle/Titanic/train.csv','rt'))
header = next(csv_file_object)
data = []
for row in csv_file_object:
	data.append(row)
	
data = np.array(data)

number_passengers = np.size(data[0::,0].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
porportion_survivors = number_survived / number_passengers
women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print ('Proportion of women who survived is %s' % proportion_women_survived)
print ('Proportion of men who survived is %s' % proportion_men_survived)

with open('C:/Users/Peter/Documents/Kaggle/Titanic/test.csv','rt') as csvTestfile:

        test_file_object = csv.reader(csvTestfile, dialect='excel')
        header = next(test_file_object)

# Open the new file so we can write to it call it something descriptive

        with open('C:/Users/Peter/Documents/Kaggle/Titanic/genderbasedmodelpy.csv','w', newline='') as csvWritefile:
                open_file_object = csv.writer(csvWritefile, dialect='excel')
                open_file_object.writerow(["PassengerId", "Survived"])

                for row in test_file_object:
                        if row[3] == 'female':

                                row.insert(1,'1')
                                open_file_object.writerow((row[0], row[1]))

                        else:
                                row.insert(1,'0')
                                open_file_object.writerow((row[0], row[1]))

                

import os

import pandas as pd
import numpy as np
import os
import numpy as np
import pandas as pd

stud_marks = ([[67,45], [90,92],[66,72],[32,40]])

#print("student marks in two subject:",np.array( stud_marks))
#Now if you have to update subject marks of each list how you can do this
stud_marks +=[5,10]
print("updated marks :", stud_marks)

student_marks = [78,92,36,64,89]
stud_marks = np.array(student_marks)

print("sum of marks =",np.sum(stud_marks))
add_arr = [2,2,5,10,2]
updated_arr = (student_marks + add_arr)
print("updated  array = ", updated_arr)


file_path = 'infodata.csv'

df = pd.read_csv(file_path)

print(df)
print(np.array(df['horsepower']))


car_arr = [[130,165,150,150,140,198,220,215,225,190,170,160,150,225],
  [95,  95,  97,  85, 88, 46,87,  90,  95, 113,  90, 215, 200, 210],
 [19, 88, 90,  95,100, 105, 100,  88, 100, 165, 175, 153, 150,32]]

car = np.array(car_arr, dtype = float)
print(car.shape)
print(car.dtype)


#Accessing elements from a 2D array

#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])

# print horsepower is > 150
data  = np.array(horsepower)
x=np.where(data >= 150)

print("sorted array:",np.sort(data))



# Find the mean and median of horsepower
print("mean of horsepower from :",np.mean(horsepower))
print("median of horsepower: ",np.median(horsepower))

# Find the min and max value 

print("min value:",np.min(horsepower))
print("max value :",np.max(horsepower))

# find the index of min and max

print("max index is :",np.argmax(horsepower))
print("min index is :",np.argmin(horsepower))


"""
Problem Statement:
Lee decides to walk 10000 steps every day to combat the effect that lockdown has had on his body’s agility, mobility, flexibility and strength. Consider the following data from fitness tracker over a period of 10 days

Day number  Steps walked

1        6012

2        7079

3        6886

4        7230

5        4598

6        5564

7        6971

8        7763

9        8032

10       9569



-Represent the above data in a 10x2 array. In each row, the first element should contain day number and second element should contain steps walked.
-Lee notices that the tracker’s battery dies every day at 7 pm. Lee discovers that on an average, he walks 2000 steps every day after 7 pm. Perform an appropriate operation on your array to add 2000 steps to all the observations.
-Write a program that returns the steps walked if the steps walked are more than 9000.
-Print an array containing steps walked in sorted order.


"""


import numpy as np


day = [1,2,3,4,5,6,7,8,9, 10]
lee_steps = [6012, 7079,6886,7230,4598,5564,6971,7763,8032,9569]
data =np.column_stack( [day , lee_steps])
#print(data)
updates_lee = np.array(lee_steps)+2000
updated_data =np.column_stack((day , updates_lee))
#print(updated_data)

steps  = np.where(updates_lee >= 9000)
#print(updated_data[steps])

#print data in sorted array
print(np.sort(updates_lee))
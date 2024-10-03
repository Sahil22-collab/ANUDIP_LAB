#Task 2 : Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.

# Importing the pandas library to work with DataFrame
import pandas as pd
# Importing numpy library to handle missing values using np.nan
import numpy as np

# Creating a dictionary called 'exam_data'
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# Creating a DataFrame from the exam_data dictionary.
# We are also assigning custom index labels (a to j) to the rows.
results = pd.DataFrame(exam_data,index=['a','b','c','d','e','f','g','h','i','j'])

# Printing the DataFrame to display it
print(results)

"""
OUTPUT :
       name  score  attempts qualify
a  Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c  Katherine   16.5         2     yes
d      James    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes
"""

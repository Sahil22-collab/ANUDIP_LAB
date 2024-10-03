#Task 1 :  Write a Pandas program to create a dataframe from a dictionary and display it.

# Importing the pandas library to work with data structures like DataFrame
import pandas as pd

# Creating a dictionary with subjects as keys and a list of scores as values
score={'Math':[78,85,96,80,86], 'English':[84,94,89,83,86],'Hindi':[86,97,96,72,83]}

# Converting the dictionary into a DataFrame
stud_score = pd.DataFrame(score)

# Displaying the DataFrame
print(stud_score)

"""
OUTPUT :
   Math  English  Hindi
0    78       84     86
1    85       94     97
2    96       89     96
3    80       83     72
4    86       86     83
"""

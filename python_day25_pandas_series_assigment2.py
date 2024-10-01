#Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. You have recorded the scores of your students for a recent exam, and
#you want to represent this data using a Pandas Series.


import pandas as pd

# Input data for household expenses
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series
expenses_series = pd.Series(expenses, index=categories)

# Display the series
print(expenses_series)


'''output
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64 '''

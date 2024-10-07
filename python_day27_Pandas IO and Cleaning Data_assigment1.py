#Task 1: Write a Pandas program to detect missing values of a given DataFrame. 
"""Input: df = pd.DataFrame({ 'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10' ,'2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'], 
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})"""

# Importing the pandas library, which is used for data manipulation and analysis.
import pandas as pd

# Importing the numpy library, mainly used here to represent missing values (NaN).
import numpy as np

# Creating a DataFrame using pandas with various columns: 'ord_no', 'purch_amt', 'ord_date', 'customer_id', and 'salesman_id'.
# Some values are missing (represented by np.nan).
df = pd.DataFrame({ 
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],  # Order number, with some missing values (np.nan).
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],  # Purchase amount.
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],  # Order date, with some missing dates (np.nan).
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],  # Customer ID.
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]  # Salesman ID, with some missing values (np.nan).
})

# Using the isnull() method to detect missing values (NaN) in the DataFrame.
# This will return a DataFrame of the same shape where each element is either True (if it's missing) or False (if it's not missing).
missing_values = df.isnull()

# Printing out the DataFrame showing the locations of missing values (True for missing, False for present values).
print("Missing values in the DataFrame:")
print(missing_values)

# Counting the number of missing (NaN) values in each column using the sum() function.
# This sums up the True values (which are treated as 1) for each column, giving us the count of missing values per column.
missing_count = df.isnull().sum()

# Printing out the count of missing values for each column.
print("Missing count in the DataFrame:")
print(missing_count)

"""
OUTPUT :
Missing values in the DataFrame:
    ord_no  purch_amt  ord_date  customer_id  salesman_id
0    False      False     False        False        False
1     True      False     False        False        False
2    False      False      True        False        False
3    False      False     False        False         True
4     True      False     False        False        False
5    False      False     False        False        False
6     True      False     False        False        False
7    False      False     False        False         True
8    False      False     False        False        False
9    False      False     False        False        False
10    True      False     False        False        False
11   False      False     False        False         True
Missing count in the DataFrame:
ord_no         4
purch_amt      0
ord_date       1
customer_id    0
salesman_id    3
dtype: int64
"""

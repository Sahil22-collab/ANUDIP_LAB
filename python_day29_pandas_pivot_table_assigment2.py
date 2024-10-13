# 2 Write a Pandas program to create a Pivot table and find the item wise unit sold.

import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'c:\Users\User\Downloads\salesdata.csv'
data = pd.read_csv(file_path)
# Create a pivot table for item-wise units sold
pivot_table_items = pd.pivot_table(data, 
                                   values='Units',  # The column to aggregate (units sold)
                                   index=['Item'],  # Grouping by item
                                   aggfunc='sum')  # Summing the units sold

# Display the resulting pivot table
pivot_table_items

'''
Output:- Item	        Units
         Cell Phone     278
         Desk	        10
         Home Theater   722
         Television     716
         Video Games    395'''

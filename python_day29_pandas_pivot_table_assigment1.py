#1 Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Admin\Desktop\salesdata.csv'
data = pd.read_csv(file_path)
# Create a pivot table for total sales amount region-wise, manager-wise, and salesman-wise
pivot_table_sales = pd.pivot_table(data, 
                                   values='Sale_amt',  # The column to aggregate (total sales amount)
                                   index=['Region', 'Manager', 'SalesMan'],  # Grouping by region, manager, and salesman
                                   aggfunc='sum')  # Summing the sales amounts

# Display the resulting pivot table
pivot_table_sales

'''
Output:- Region	Manager	SalesMan    Sale_amt
        Central	Douglas	John        124016.0
                Hermann	Luis	    206373.0
                        Shelli	    33698.0
                        Sigal	    125037.5
                Marth	Steven	    14000.0
                Martha	Steven	    185690.0
                Timothy	David	    140955.0
        East	Douglas	Karen	    48204.0
                Martha	Alexander   236703.0
                        Diana	    36100.0
        West	Douglas	Michael	    66836.0
                Timothy	Stephen	    88063.0
'''

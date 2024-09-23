import numpy as np  # Importing the NumPy library for numerical operations

# Revenue data for two product categories
category1_revenue = np.array([500, 600, 700, 550])  # Revenue for category 1
category2_revenue = np.array([450, 700, 800, 600])  # Revenue for category 2

# Calculate total revenue by adding corresponding elements of both arrays
total_revenue = category1_revenue + category2_revenue

# Print the total revenue for each category
print("Total Revenue:", total_revenue)

'''output
Total Revenue: [ 950 1300 1500 1150]
'''

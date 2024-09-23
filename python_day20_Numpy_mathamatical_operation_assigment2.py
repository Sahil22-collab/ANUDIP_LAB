import numpy as np  # Importing the NumPy library for numerical operations

# Revenue and expenses data for the company
revenue = np.array([10000, 12000, 11000, 10500])  # Revenue for each period
expenses = np.array([4000, 5000, 4500, 4800])     # Expenses for each period

# Calculate profit by subtracting expenses from revenue
profit = revenue - expenses

# Print the profit for each period
print("Profit:", profit)

'''output
Profit: [6000 7000 6500 5700]
'''

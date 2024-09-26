# Task 1: Bar Chart to Represent Monthly Expenses in Different Spending Categories

# Importing necessary libraries
import matplotlib.pyplot as plt

# Input data: Spending categories and corresponding expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create the bar chart
plt.bar(categories, expenses)

# Add labels and title
#Adding x-axis label
plt.xlabel('Spending Categories')      

#Adding y-axis label
plt.ylabel('Monthly Expenses (in dollars)')

#Adding Title of the Bar Chart or Bar Plot
plt.title('Monthly Expenses by Category')

# Show the plot
plt.show()

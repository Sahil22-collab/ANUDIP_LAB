#Task 1 : Create a pie chart to visualize the distribution of your monthly income by source.
#You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.

# Import the necessary library
import matplotlib.pyplot as plt

# Step 1: Define the income sources (labels for the pie chart)
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']

# Step 2: Define the monthly income corresponding to each source
monthly_income = [5000, 1500, 1000, 600, 400]

# Step 3: Create the pie chart
# - 'monthly_income' is the data we want to represent in the pie chart.
# - 'labels=income_sources' will assign each income source a section of the pie.
# - 'autopct' will display the percentage of each slice on the chart, formatted to 1 decimal place.
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%')

# Step 4: Set the title of the pie chart
plt.title('Monthly Income Distribution by Source')

# Step 5: Show the pie chart
plt.show()

"""Conclusion/Analysis:
Salary contributes the most to your monthly income, accounting for 58.8%. This indicates that your primary income source is your salary.
Freelance work contributes 17.6%, showing it’s a significant but secondary source of income.
Investments account for 11.8%, suggesting that investments provide a moderate contribution.
Rental income makes up 7.1%, which is a smaller, but still notable, income source.
Other sources contribute the least, at 4.7%.
"""

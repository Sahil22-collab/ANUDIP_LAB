#Task 2 :Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time.
#You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the time period (months from 1 to 12)
months = np.arange(1, 13)

# Step 2: Define the sales data for each product category
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Step 3: Create a figure and subplots with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Step 4: Plot the sales for each category on its own subplot
# Electronics sales plot
axs[0, 0].plot(months, electronics_sales, marker="o",c="red" , label='Electronics')
axs[0, 0].set_title('Electronics Sales')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Sales ($)')
axs[0, 0].legend()

# Clothing sales plot
axs[0, 1].plot(months, clothing_sales, c='blue', marker='o' , label='Clothing')
axs[0, 1].set_title('Clothing Sales')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Sales ($)')
axs[0, 1].legend()

# Home & Garden sales plot
axs[1, 0].plot(months, home_garden_sales, marker="o",c="purple" , label='Home & Garden')
axs[1, 0].set_title('Home & Garden Sales')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Sales ($)')
axs[1, 0].legend()

# Sports & Outdoors sales plot
axs[1, 1].plot(months, sports_outdoors_sales, c='orange', marker='o' , label='Sports & Outdoors')
axs[1, 1].set_title('Sports & Outdoors Sales')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales ($)')
axs[1, 1].legend()

# Step 5: Adjust the layout and display the figure
plt.tight_layout()
plt.show()

"""
Conclusion/Analysis:

Electronics Sales:
Electronics sales show an overall upward trend, with a significant spike towards the end of the year.
Sales start at $25,000 in January and steadily increase to $42,000 by December.
This indicates a strong performance, possibly due to product launches or seasonal demand, such as holiday shopping during the year-end.

Clothing Sales:
Clothing sales show a steady but gradual increase throughout the year, from $15,000 in January to $26,000 by December.
The trend suggests stable growth, possibly reflecting consistent demand across different seasons, without significant fluctuations.

Home & Garden Sales:
Like clothing, Home & Garden sales steadily rise, starting at $18,000 in January and reaching $29,000 in December.
The category shows continuous improvement, indicating a growing market, with no significant dips or spikes during the year.

Sports & Outdoors Sales:
Sports & Outdoors sales start at $12,000 in January and gradually increase to $23,000 in December.
The growth is consistent, though this category has the lowest sales compared to the others.
This might indicate niche demand, possibly growing in popularity throughout the year.
"""

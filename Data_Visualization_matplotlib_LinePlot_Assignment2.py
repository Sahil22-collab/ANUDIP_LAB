# Task 2: Line Plot to Visualize Daily Temperature Changes Over Time in a City

# Importing necessary libraries
import matplotlib.pyplot as plt

# Input data: Days and corresponding temperatures
# 1 to 31 days of the month
days = list(range(1, 32))  
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create the line plot
plt.plot(days, temperature, marker='o', color='orange')

# Add labels and title
#Adding x-axis label
plt.xlabel('Day of the Month')

#Adding y-axis label
plt.ylabel('Temperature (°F)')

#Adding Title of Line Plot 
plt.title('Daily Temperature Changes Over Time')

# Show the plot
plt.show()

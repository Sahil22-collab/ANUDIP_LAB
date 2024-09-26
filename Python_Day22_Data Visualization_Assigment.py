import matplotlib.pyplot as plt

# Given data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Creating a line plot
plt.plot(x, y,marker='o')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot of Given Data')

# Displaying the plot
plt.show()

#Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

import numpy as np

my_list = [1, 2, 3, 4, 5]

# Convert list to NumPy array
my_array = np.array(my_list)

# Display the array
print("Array:", my_array)

# Display first and last element
print("First:", my_array[0])
print("Last:", my_array[-1])

# Multiply each element by 2 and display
print("Multiplied by 2:", my_array * 2)

'''output
Array: [1 2 3 4 5]
First: 1
Last: 5
Multiplied by 2: [ 2  4  6  8 10]'''


#Write Python program to Return a set of elements present in Set A or B, but not both.

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get the symmetric difference of both sets
unique_items = set1.symmetric_difference(set2)

# Print the result
print(unique_items)

'''OUTPUT
{20, 70, 10, 60} '''

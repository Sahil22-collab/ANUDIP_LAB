#Write a Python program to Get Only unique items from two sets. 

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get the union of both sets
unique_items = set1.union(set2)

# Print the result
print(unique_items)

'''Output
{70, 40, 10, 50, 20, 60, 30}'''


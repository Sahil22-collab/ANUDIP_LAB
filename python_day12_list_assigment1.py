# Write a Python program to sum all the items in a list.
# Function to sum all items in a list
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
total = sum_list(my_list)
print(f"The sum of the list is: {total}")

'''OUTPUT
The sum of the list is: 15'''

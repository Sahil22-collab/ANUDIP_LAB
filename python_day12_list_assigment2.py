#Write a Python program to get the largest and smallest number from a list without builtin functions. 
# Function to get the largest and smallest number from a list
def min_max(items):
    # Initialize the first item as both min and max
    smallest = items[0]
    largest = items[0]
    
    # Loop through the list to find min and max
    for item in items[1:]:
        if item < smallest:
            smallest = item
        if item > largest:
            largest = item
    
    return smallest, largest

# Example usage
my_list = [12, 45, 7, 23, 89, 3, 67]
smallest, largest = min_max(my_list)
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")

'''OUTPUT
The smallest number is: 3
The largest number is: 89
'''

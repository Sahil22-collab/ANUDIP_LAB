#Write a Python program to find duplicate values from a list and display those.
# Function to find duplicate values in a list
def find_duplicates(items):
    duplicates = []
    seen = []
    
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.append(item)
    
    return duplicates

# Example usage
my_list = [1, 2, 3, 4, 2, 5, 6, 1, 7]
duplicates = find_duplicates(my_list)
print("Duplicate values:", duplicates)

'''
OUTPUT
Duplicate values: [2, 1]
'''

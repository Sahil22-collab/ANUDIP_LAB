# 2. Write a Python program to remove duplicate characters of a given string.

# Given String

input_string = "String and String Function"

# Define function
def remove_duplicate_words(input_string):
    # Split the string into a list of words
    words = input_string.split()
    
    # Initialize an empty list to store unique words
    result = []
    # Use a set to track seen words
    seen = set()
    
    # Iterate through each word in the list
    for word in words:
        if word not in seen:
            result.append(word)
            seen.add(word)
    
    # Join the list of unique words into a string and return it
    return ' '.join(result)

# Input string


# Remove duplicates and print the result
output_string = remove_duplicate_words(input_string)
print(output_string)

#Output
"""
String and Function

"""

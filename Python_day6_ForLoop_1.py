#Q.1)Python program to check if the given string is a palindrome .

# Prompt the user to input a string and store it in the variable 'string'
string = input("Enter the string to check if is's a palindrome or not : ")

# Create a new variable 'original_string' and set it equal to the input string.
original_string = string

# Initialize an empty string called 'reverse_str' to store the reversed version of the input string.
reverse_str = ""

# Start a loop that iterates through each character in the input string.
for i in string :
    # This effectively reverses the order of characters in 'reverse_str'.
    reverse_str = i + reverse_str
# The loop completes when all characters have been processed.

# Print the reversed string.
print("Reversed String :", reverse_str)

# Compare the reversed string with the original input string.
if (reverse_str == original_string):
    print("The string is a palindrome.")
else :
    print("The string is not a palindrome.")
# If they are the same, it's a palindrome; otherwise, it's not.

"""
when i run program 1st time the output is below
OUTPUT : Enter the string to check if is's a palindrome or not : madam
Reversed String : madam
The string is a palindrome.


when i run program 2nd time the output is below
OUTPUT :Enter the string to check if is's a palindrome or not : python
Reversed String : nohtyp
The string is not a palindrome.
"""














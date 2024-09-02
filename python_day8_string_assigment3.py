#Q.3)Write a Python program to reverse words in a string 

# Original string.
string = "Deeptech Python Training"

# Split the string into words and reverse the list of words and join them back.
# The reversed() function returns an iterator that yields the words in reverse order
#The join() method concatenates the elements of the reversed list into a single string, separated by spaces
reversed_string = ' '.join(reversed(string.split()))

# Display the string with words in reverse order.
print("Reversed words :",reversed_string)


"""
OUTPUT :
Reversed words : Training Python Deeptech
"""


#Q.2) Write a Python program to remove a newline in Python.

# Original string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Replace newline characters with a space and remove any leading/trailing spaces
cleaned_string = string.replace("\n", " ").strip()

# Display the cleaned string without newlines
print("String without newlines : ")

# Print the actual cleaned string that has had all newline characters removed
print(cleaned_string)

"""
OUTPUT : String without newlines : 
Best  Deeptech  Python  Training
"""

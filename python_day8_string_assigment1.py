#Q.1)Write a Python program to count the occurrences of each word in a given sentence.

# Original string
string = "To change the overall look of your document. To change the look available in the gallery."

# Clean the string by removing non-alphanumeric characters and converting to lowercase
cleaned_string = ''.join(char for char in string if char.isalnum() or char.isspace()).lower()

# Initialize an empty dictionary to store word counts
word_counts = {}

# Split the cleaned string into words
for word in cleaned_string.split():
    
    # Update the word count in the dictionary
    word_counts[word] = word_counts.get(word, 0) + 1

# Print the word occurrences
print("Word occurrences : ")

# Loop through each key-value pair in the word_counts dictionary
# 'word' is the key (the actual word), and 'count' is the value (the number of occurrences of that word)
for word, count in word_counts.items():
    
# Print the word and its count in the format "word: count"
# The f-string allows for embedding variables directly within the string
    print(f"{word}: {count}")


"""
OUTPUT : Word occurrences : 
to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1
"""










    

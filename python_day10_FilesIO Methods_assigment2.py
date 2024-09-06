#  Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename):
    '''
    Counts and displays the total number of words in a text file.

    :param filename: Name of the file to read.
    :return: Total number of words in the file.
    '''
    total_words = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
        
        print(f"Total number of words in '{filename}': {total_words}")
        return total_words
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Calling a function
count_words_in_file("ABC.txt")

#Ouput

'''
Total number of words in 'ABC.txt': 10

'''

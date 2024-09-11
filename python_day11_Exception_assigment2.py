# Function to prompt the user for an integer and handle invalid inputs
def integer_input():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print(f"You entered the integer: {number}")
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer. Please enter a valid integer.")

# Example usage
integer_input()

'''Output
Enter an integer: 4
You entered the integer: 4

Enter an integer: anit
Error: 'anit' is not a valid integer. Please enter a valid integer.'''

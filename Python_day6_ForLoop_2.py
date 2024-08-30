# Python program to check if the number is an Armstrong number or not

# Function to check if a number is an Armstrong number using a for loop
def is_armstrong(number):

    # Calculate the number of digits
    num_digits = len(str(number))

    # Initialize a variable to store the sum of digits raised to the power of num_digits
    total = 0

  # Loop through each digit in the number (as a string)
    for digit in str(number):

        # Convert the digit back to an integer and raise it to the power of num_digits
        total = total + int(digit) ** num_digits

    # Check if the number is equal to the sum of its digits raised to the power of the number of digits
    return number == total

# Take input from the user
user_number = int(input("Enter a number : "))

# Check if the number is an Armstrong number and print the result
if is_armstrong(user_number):
    print(f"The Number {user_number} is an Armstrong number !")
else :
    print(f"The Number {user_number} is not an Armstrong number !")

"""
OUTPUT : Enter a number : 153
The Number 153 is an Armstrong number !


OUTPUT : Enter a number : 412119
The Number 412119 is not an Armstrong number !
"""







  

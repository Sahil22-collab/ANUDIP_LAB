#Q2.Write a python program finding the factorial of a given number using a while loop
def factorial(n):
    # Check if the input number is negative
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = 1
        
        # Calculate factorial using a while loop inside the else block
        while n > 0:
            result *= n
            n -= 1
        
        print(f"The factorial is {result}.")

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate the factorial of the entered number
factorial(number)

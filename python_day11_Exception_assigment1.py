# Function to divide two numbers and handle division by zero
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

divide_numbers(num1, num2)

'''OUTPUT
Enter the numerator: 10
Enter the denominator: 3
The result of 10.0 / 3.0 is 3.3333333333333335

Enter the numerator: 10
Enter the denominator: 0
Error: Division by zero is not allowed.'''

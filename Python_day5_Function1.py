# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a, b):
    # Check if the denominator is not zero to avoid division by zero error
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division by zero is not allowed.")

# Example usage
div(10, 2)  # This will print: Division: 5.0
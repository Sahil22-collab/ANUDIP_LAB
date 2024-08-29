#Q1.Write a python program to check whether a number is palindrome or not? 
def is_palindrome(num):
    # Store the original number
    original_num = num
    reversed_num = 0

    # Reverse the number using a while loop
    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num = num // 10

    # Check if the reversed number is the same as the original number
    return reversed_num == original_num

number = int(input("Enter a number: "))

# Determine if the number is a palindrome and print the result
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

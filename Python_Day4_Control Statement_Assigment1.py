#Q.1)Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

#Enter the number
number = int(input("Enter the Numbers : "))

# If else logic experssion
if number % 2 == 0:
    print("The Number is Even")

else :
    print("The Number is Odd")

"""
When we put 11 the output is odd.
OUTPUT : Enter the Numbers : 11
         The Number is Odd

When we put 12 the output is even.
OUTPUT : Enter the Numbers : 12
         The Number is Even.
"""

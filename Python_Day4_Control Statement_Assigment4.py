#Q.4) Create a Python program that checks if a user-given number is positive, negative, or zero.

#enter the number 
number = int(input("Enter the number : "))

#LADDER IF ELSE Logic Expression
if number > 0:
    print("The Number is Positive")
elif number < 0:
    print("The Number is Negative")
else :
    print("The Number is Zero")


"""
when i enter 1 then output is,
OUTPUT :Enter the number : 1
        The Number is Positive

when i enter -5 then output is,
OUTPUT : Enter the number : -5
         The Number is Negative

when i enter 0 then output is,
OUTPUT : Enter the number : 0
         The Number is Zero
"""

    

#Q.5) Write a Python program that determines the largest of three.

#Enter Three Numbers
num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the Second number : "))
num3 = int(input("Enter the Third number : "))

#LADDER IF ELSE Logic Expression
if num1 >= num2 and num1 >=num3:  
    print(f"The Largest number is : {num1}")  #F-strings make it easy to see the relationship between the variables and the text.
if num2 >= num3 and num2 >=num1:
    print(f"The Largest number is : {num2}")
else:
    print(f"The Largest number is : {num3}")

"""
OUTPUT : Enter the First number : 11
         Enter the Second number : 31
         Enter the Third number : 2
         The Largest number is : 31
"""
    

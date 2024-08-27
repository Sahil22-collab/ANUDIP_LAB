#Q.3) Write a Python program that determines if a given year is a leap year or not.

#Enter the year
year = int(input("Enter a year: "))

#IF ELSE logic expression
"""A year is a leap year if:
    It is divisible by 4.
    It is not divisible by 100, unless it is also divisible by 400."""
if (year % 4 == 0 and year % 100 != 0): 
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


"""
When i put year 2024 the output is given below,
OUTPUT : Enter a year: 2024
         2024 is a leap year.

When i put year 2024 the output is given below,
OUTPUT : Enter a year: 2023
         2023 is not a leap year.
"""

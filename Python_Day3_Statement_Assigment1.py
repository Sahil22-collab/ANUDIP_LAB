#Q.1) Using input() function take one number from the user and using ternary operators check whether the number is even or odd

#input the number
num = int(input("Enter the Numbers : "))

#if and else logic applied
result = "Even" if num % 2 == 0 else  "odd"

#for output
print("The Number is : ", result)


"""
when we put 6 then the output is 
OUTPUT : Enter the Numbers : 6
                 The Number is :  Even

when we put 5 then the output is
OUTPUT : Enter the Numbers : 5
                 The Number is :  odd
"""

#Q.2. Using input function take two number and then swap the number

#input the two numbers
num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))

#before swapping numbers
print("Before Swapping num1 = ", num1 , " And num2 =", num2)

#swapping of two numbers
num1, num2 = num2, num1

#afetr swapping numbers 
print("After Swapping num1 = ", num1 , "And num2 =", num2)


"""
OUTPUT : Enter the first Number : 11
                 Enter the second Number : 2
                 Before Swapping num1 =  1  And num2 = 2
                 After Swapping num1 =  2 And num2 = 1
"""

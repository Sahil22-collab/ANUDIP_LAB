#Q.2)Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

#enter the age
age = int(input("Enter Your Age : "))

# IF ELSE Logic expression 
if age >= 18 :
    print(" Congrualtions, Your are eligible for Vote ")
else :
    print(" Sorry, Your are not eligible for Vote ")


"""
when i put 17 then the output is given below
OUTPUT : Enter Your Age : 17
         Sorry, Your are not eligible for Vote


when i put 20 then the output is given below
OUTPUT : Enter Your Age : 20
         Congrualtions, Your are eligible for Vote
"""

# >>>>>>>>>>>>>>>>>>>> Conditional statements in Python >>>>>>>>>>>>>>>
#  IF statement
# if -else statement
# if -elif statements


#  if statement
"""      
             The if statement is used to excute a soecific condition ,
             if the given condition is true , a block of code will be excuted 

"""
#  Example of if statement
age = 18
if age >= 18:
    print(" your are eligible for vote ")

# output is
"""
your are eligible for vote
"""


# if -else statement

"""
             The if-else  statement is same to if statement , 
             but when if statement condition is false then the else statement will be excuted 
     
"""

#  Example for if-else statement

age = 17
if age >= 18:
    print(" your are eligible for vote ")
else:
    print("Your are not eligible for vote")


# output is
"""
Your are not eligible for vote
"""


# if elif statement or nested if satements

"""
The if-elif  statement is same to if statement , 
  but when if statement condition is false then the elif statement will be excuted 
      
  it is used  when we pass for mulitiple conditions   

"""

#  Example for nested if statement

marks = 90
if marks >= 90:
    print("you have  achived very very good score , you get A++ grade")
elif marks == 80:
    print(" you have achied  very good score ,you get A+ garde")
elif marks >= 60 and marks <= 70:
    print(" you have achieved good score, you get B++ garde")
elif marks <= 50 and marks >= 40:
    print(" you have achieved  very low score , you get B grade")
else:
    print("you have achieved  very low score , you get C grade")

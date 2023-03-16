#  >>>>>>>>>>>>>>>>>  Operatorators in python >>>>>>>>>>>>>>>>>>>>

#  Arthimetic Operators
#  Assignmen  Operators
#  Comparision Operators
#  Logical   Operators
#  Ternary   Operators


#    >>>>>>>>>>>>>   Arthimetic Operators  >>>>>>>>>>>>>>>>>>>>

print(15 + 5)         # Addition operator (+)
print(10 - 5)         # Subtraction operator (-)
print(15 / 5)         # Division operator (/)
print(10 // 2)        # Floor division operator (//)
print(15 * 5)         # Multiplication  operator (*)
print(15 % 5)         # Modulus or Reminder operator (%)
print(2 ** 5)         # Exponential  operator (**)

# Output

"""
20
5
3.0
5
75
0
32
"""


#    >>>>>>>>>>>>>   Assignment Operators  >>>>>>>>>>>>>>>>>>>>

#   (=) Equal operator
a = 10
b = 30
print(a)
print(b)

# output
"""
10
30
"""

#   (+=) Incriment or addition
a = 20
b = 40
print(a, b)

b += a
print(b)

# output
"""
20 40
60

"""

#  (-=) Decriment or subtraction

a = 50
b = 10
print(a, b)

a -= b
print(a)

# output
"""

50 10
40
"""

#  (/=) Division

a = 40
b = 20
print(a, b)

a /= b
print(a)

# output
"""
40 20
2.0
"""

#  (//=)  floor Division
a = 40
b = 20
print(a, b)

a //= b
print(a)

# output
"""
40 20
2
"""

#  (*=) Multiplication

a = 40
b = 20
print(a, b)

a *= b
print(a)

# output
"""
40 20
800
"""


#    >>>>>>>>>>>>>   Comparison Operators  >>>>>>>>>>>>>>>>>>>>

# (==) Equal
# (!=) Not Equal
# (>)  Greaterthan
# (<) Lessthan
# (>=) Greater than eaqual
# (<=) Lessthan equal

print(15 == 10)
print(15 > 10)
print(15 < 10)
print(15 >= 10)
print(15 <= 10)
print(15 != 10)

# Output
"""
False
True
False
True
False
True
"""


#    >>>>>>>>>>>>>   Logical Operators  >>>>>>>>>>>>>>>>>>>>

#  AND
#  Returs True if both statements or true


#             >>>>> Example1  >>>>>>

#   if only one statement is true so it will excute else statement

student_name = True
roll_number = False
if student_name and roll_number:
    print(" Go to exam hall room ,  Good luck >>")
else:
    print("Sorry check your number, try again !!")


# Output
    """
    Sorry check your number, try again !!
    """


#            >>>>> Example2 >>>>>>

    #  if two  statement are true so it will excute if  statement

student_name = True
roll_number = True
if student_name and roll_number:
    print(" Go to exam hall room ,  Good luck >>")
else:
    print("Sorry check your number, try again !!")

    # Output
    """
    Go to exam hall room ,  Good luck >>
    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#  OR

#  Returs true if oneof the  statement is  true

#        >>>>> Example1  >>>>>>

#   if only one statement is true so it will excute if statement

student_name = True
roll_number = False
if student_name or roll_number:
    print(" Go to exam hall room ,  Good luck >>")
else:
    print("Sorry check your number, try again !!")


# Output
    """
   Go to exam hall room ,  Good luck >>
    """


#               >>>>> Example2 >>>>>>

    #  if two  statement are true so it will excute else   statement

student_name = False
roll_number = False

if student_name and roll_number:
    print(" Go to exam hall room ,  Good luck >>")
else:
    print("Sorry check your number, try again !! ")

    # Output
    """
    Sorry check your number, try again !!
    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# NOT

# it is reverse the result and returs false if the resultis true


#               >>>>> Example1 >>>>>>

    #  if one  statement are false so it will excute if    statement

student_name = True
roll_number = False
if not roll_number:
    print("Sorry check your number, try again !! ")

# in if statement if the cindition is true it  will run ,
   # so inthis roll nuber is false thats why it run if staement

else:
    print(" Go to exam hall room ,  Good luck >>")

    # Output
    """
    Sorry check your number, try again !!
    """


#                      >>>>> Example1 >>>>>>

    #  if two   statement are true so it will excute else    statement

student_name = True
roll_number = True
if not roll_number:
    print("Sorry check your number, try again !! ")

# in if statement if the cindition is true it  will run ,
   # so inthis roll nuber is true, but we not is used  to reverse the result   thats why it run else  staement

else:
    print(" Go to exam hall room ,  Good luck >>")

    # Output
    """
    Go to exam hall room ,  Good luck >>
    """
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#    >>>>>>>>>>>>>   Ternary Operators  >>>>>>>>>>>>>>>>>>>>

# This operator is used to replace the multiple line of if else statements
#  This is a single line statement


#                    >>>>>> Example1 >>>>>>>

age = 18
result = "Your are eligible for vote" if age >= 18 else "sorry not eligible for vote "
print(result)


# out put
"""
Your are eligible for vote
"""


#                      >>>>>> Example2 >>>>>>>

age = 17
result = "Your are eligible for vote" if age >= 18 else "sorry not eligible for vote "
print(result)


# out put
"""
 sorry your arenot  eligible for vote
"""

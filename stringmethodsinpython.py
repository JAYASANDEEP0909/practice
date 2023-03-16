
# >>>>>>>>>>>>>> String methods in python >>>>>>>>>>>>>>>

#  In python wecan perform different methods on strings
#   we can access string methods by entering dot(.) to the variables

#  len()    --------  in this method  used to  extract the length of string characters

my_name = "Anupamasandy"
print(my_name)
print(len(my_name))

#  Output

"""
Anupamasandy
12

"""


#  Index notation [] ----- in this method we can perform by using index numbers  to extract specifed string
my_name = "Anupamasandy"
print(my_name)
print(my_name[0])
print(my_name[0:3])
print(my_name[4:6:])
print(my_name[:])
print(my_name[:-1])
print(my_name[-1:])

#  Output

"""
Anupamasandy
A
Anu
am
Anupamasandy
Anupamasand
y

"""

#  title()------- In this method  first letter of character in string is  capitalized
student = "person"
print(student)
print(student.title())


#  Output

"""
person
Person

"""


#  upper()      ------- In this method  all  letters of characters in string is  capitalized
student = "person"
print(student)
print(student.upper())


#  Output

"""
person
PERSON

"""


#  lower()------- In this method  all letters of characters in string is  lower-capitalized
student = "PERSON"
print(student)
print(student.lower())


#  Output

"""
PERSON
person

"""


#  strip() --- in this method  it removes the extra  space in string

movie = "      Ironman, it is marvel movie     "
print(movie)
print(movie.strip())
# rstrip - RIGHTSTRIP in this it remove the rigt side space of string
print(movie.rstrip())
# lstrip - LEFTSTRIP in this it remove the left side space of string
print(movie.lstrip())


#  Output

"""
      Ironman, it is marvel movie     
Ironman, it is marvel movie
      Ironman, it is marvel movie
Ironman, it is marvel movie     


"""


#  find() --- in this method we can find the specific string characters
python = " python is a object oreinted program"
print(python)
print(python.find("ob"))

#  Output

"""
 python is a object oreinted program
13

"""


#  replace()  ----- in this method we can replace a string characters at specific place  by passing two arguments
__name__ = "jayasandeep"
print(__name__)
print(__name__.replace("jaya", "anupama"))


#  Output

"""
jayasandeep
anupamasandeep

"""


#  Format string --- inthis method wecan format the string
# for adding two string reada bility of string is difficult so at the time we use format
#  lets see

#  Concanent a string  by (+) operator
country = "INDIA"
state = "ANDHRA PARADESH"
print("country is " + country + " and " + " the state is " + state)


#  Output

"""
country is INDIA and  the state is ANDHRA PARADESH


"""
#   by using format
country = "INDIA"
state = "ANDHRA PARADESH"
print(f"country is {country} and the  state is {state}")

#  Output

"""
country is INDIA and  the state is ANDHRA PARADESH

"""


#   In string more methods are there  , these are some common methods used in python

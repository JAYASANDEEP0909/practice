#   >>>>>>>>>>> Python  Data types  >>>>>>>>>>>>>>>


#  Data type                              # Class            # Value

#  1. Numeric type

#   Integer number                     int                 55

#  Floating point number               float               55.000

#  Complex number                      complex              1+3j

# 2. Boolean type                           bool                True or False

# 3. Strings                                str                 " my name is "

# 4. List                                   list                  [ "apple" 45, "name", "fruit"]

# 5. Tuple                                  tuple                  ( "name","number",1234)

# 6. Dictionary                             dict                   {user id :"sandeep",1:"name",id:"1234"

# 7.  Set                                    set                    { "apple" 45, "name", "fruit"}


#  Data types are building block of code


#                          >>>>>>>>>>>>>> NUMERIC DATA TYPES >>>>>>>>.>

#     >>>>>>>> Integer number >>>>.>>>>>>
my_age = 18
print(my_age)
print(type(my_age))

#  Output
"""
18
<class 'int'>

"""

#     >>>>>>>> Floating point number >>>>.>>>>>>
my_grade = 7.9
print(my_grade)
print(type(my_grade))

#  Output
"""
7.9
<class 'float'>

"""
#     >>>>>>>> complexnumber >>>>.>>>>>>

complex_number = 5+3j
print(complex_number)
print(type(complex_number))

#  Output
"""
(5+3j)
<class 'complex'>


"""

#                       >>>>>>>...  BOOLEAN DATA TYPE >>>>>>>>>>>>>>

name = True
grade = False
print(name)
print(grade)
print(type(name))
print(type(grade))

#  Output
"""
True
False
<class 'bool'>
<class 'bool'>

"""


#        >>>>>>>>>>>>>>> STRING DATA TYPE >>>>>>>>>>>>


my_name = " your name "
print(my_name)
print(type(my_name))

#  Output
"""
 your name 
<class 'str'>

"""


#         >>>>>>>>>>>>> LIST DATA TYPES >>>>>>>>>>>>

my_list = ["apple", "45", "name", "fruit"]
print(my_list)
print(type(my_list))

#  Output
"""
 ['apple', '45', 'name', 'fruit']
<class 'list'>

"""


#         >>>>>>>>>>>>> TUPLE DATA TYPES >>>>>>>>>>>>

my_tuple = ("apple", "45", "name", "fruit")
print(my_tuple)
print(type(my_tuple))

#  Output
"""
('apple', '45', 'name', 'fruit')
<class 'tuple'>
"""


#         >>>>>>>>>>>>> DICTIONARY  DATA TYPES >>>>>>>>>>>>

my_dict = {"fruit": "apple", "id": "45", "student": "name"}
print(my_dict)
print(type(my_dict))

#  Output
"""
 {'fruit': 'apple', 'id': '45', 'student': 'name'}
<class 'dict'>

"""


#         >>>>>>>>>>>>> SET DATA TYPES >>>>>>>>>>>>

my_set = {"apple", "45", "name", "fruit"}
print(my_set)
print(type(my_set))

#  Output
"""
{'name', 'apple', '45', 'fruit'}
<class 'set'>

"""


#  List methods
#  Python has a set of built in method for list

#  list()    we can use list method to create list

student = list("person")
print(student)

# output
"""
['p', 'e', 'r', 's', 'o', 'n']
"""


# ****.....    index()  or [] .....>>>>>> in this method  we can returs the elmets based on their index value

country_nmaes = ["india", "usa", "canada", "nepal", "china"]
print(country_nmaes)

print(country_nmaes[0])
print(country_nmaes[3])
print(country_nmaes[1])

country_nmaes[2] = "japan"
print(country_nmaes)

# out put
"""
['india', 'usa', 'canada', 'nepal', 'china']

india

nepal

usa

['india', 'usa', 'japan', 'nepal', 'china']

"""

#  step
print(country_nmaes[1:4])
print(country_nmaes[0:3])
print(country_nmaes[:4])

# output
"""
['usa', 'japan', 'nepal']

['india', 'usa', 'japan']

['india', 'usa', 'japan', 'nepal']

"""


# ****.....range() .....>>>>>>

numbers = list(range(50))
print(numbers)

# output
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
41, 42, 43, 44, 45, 46, 47, 48, 49]

"""


# ****.....  append() in this method   we can add elements  at the end of list  .....>>>>>>

#  append(element)---- syntax
movies = ["Ironman1", "Ironman2"]
print(movies)
movies.append("Ironman3")
print(movies)


# output
"""
['Ironman1', 'Ironman2']

['Ironman1', 'Ironman2', 'Ironman3']

"""


# ****.....    insert()  it opposit to append method  , in this we  insert element at specified position .....>>>>>>

#  insert(position , element)---- syntax

numbers = list(range(10))
print(numbers)
numbers.insert(5, "marvel")
numbers.insert(8, 34556)
print(numbers)

# out put
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[0, 1, 2, 3, 4, 'marvel', 5, 6, 34556, 7, 8, 9]

"""


# ****..... pop()   it removes the elemet at specified position when we pass .....>>>>>>
#  otherwise it it revoves end of list

numbers1 = [123, 456, 789, 765, 908]
print(numbers1)


numbers1.pop()
# print(numbers1)

# output
"""
[123, 456, 789, 765, 908]

[123, 456, 789, 765]

"""
numbers1.pop(0)
numbers1.pop(2)

# output
"""
[123, 456, 789, 765, 908]

[456, 789]
"""

print(numbers1)


# ****.....remove()     remove the items with specified value      .....>>>>>>

country_nmaes = ["india", "usa", "canada", "nepal", "china"]
print(country_nmaes)
country_nmaes.remove("china")
print(country_nmaes)
# output
"""
['india', 'usa', 'canada', 'nepal', 'china']

['india', 'usa', 'canada', 'nepal']
"""

#  del()  in this method we can  remove the items  inthe form of range of items , specify the index number

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
print(num)
del num[1:3]
del num[:4]
print(num)

# output
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[6, 7, 8, 9, 10]
"""

# clear()    ---- it removes all the items in a list
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
print(num)

num.clear()
print(num)

# output
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[]

"""

#  reverse() --- it reverse the items inthe list

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
print(num)

num.reverse()
print(num)

# output
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""

# join ()  join the list of items in a list

movies = ["Ironman1", "Ironman2", "Ironman3"]
print(movies)

print("". join(movies))
print(" ". join(movies))
print(" , ". join(movies))

# output
"""
['Ironman1', 'Ironman2', 'Ironman3']

Ironman1Ironman2Ironman3

Ironman1 Ironman2 Ironman3

Ironman1 , Ironman2 , Ironman3

"""
# sort() ------ order the list either ASC OR DESC

#  for  asc orderd list just call the sort method

country_nmaes = ["india", "usa", "canada", "nepal", "china"]
print(country_nmaes)

country_nmaes.sort()
print(country_nmaes)

# output
"""
['india', 'usa', 'canada', 'nepal', 'china']

['canada', 'china', 'india', 'nepal', 'usa']

"""

# for desc oreder sort( key = true)

country_nmaes.sort(reverse=True)
print(country_nmaes)

# output

['canada', 'china', 'india', 'nepal', 'usa']

['usa', 'nepal', 'india', 'china', 'canada']

#  sorted () ---

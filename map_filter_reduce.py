"""
map():
"A map function executes certain instructions or functionality provided to it on every item of an iterable."

The iterable could be a list, tuple, set, etc. It is worth noting that the output in the case of the map is also an iterable i.e., a list.
It is a built-in function, so no import statement required.

SYNTAX:
map(function, iterable)
A map function takes two parameters:
First one is the function through which we want to pass the items/values of the iterable
The second one is the iterable itself
"""


# MAP FUNCTION


def sq(z):
    return z * z


numbers = ["1", "2", "3", "4", "5"]
numbers = list(map(int, numbers))  # converts the list objects into integers
square = list(map(sq, numbers))  # converts the list objects to their squares
print(square)


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


func = [square, cube]
for i in range(100):
    val = list(map(lambda x: x(i), func))
    print(val)

# Example:
items = [1, 2, 3, 4, 5]
o = list(map((lambda x: x ** 3), items))
print(o)
# Output: [1, 8, 27, 64, 125]
# The map()function passes each element in the list to a lambda function and returns the mapped object.
"""
filter():-
"A filter function in Python tests a specific user-defined condition for a function and returns an iterable for the elements and values that satisfy the 
condition or, in other words, return true."

It is also a built-in function, so no need for an import statement. All the actions we perform using the filter can also be performed by using a for loop 
for iteration and if-else statements to check the conditions. We can also use a Boolean that could take note of true or false, but that would make the 
process very lengthy and complex. So, to simplify the code, we can use the filter function.

SYNTAX:
filter(function, iterable)
It also takes two parameters:

First one is the function for which the condition should satisfy
The second one is the iterable"""
# FILTER FUNCTION
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_than(num):
    return num > 5


greater_than_5 = list(filter(is_greater_than, list_2))
print(greater_than_5)

# Example:
a = [1, 2, 3, 4, 5, 6]
b = [2, 5, 0, 7, 3]
c = list(filter(lambda x: x in a, b))
print(c)  # prints out [2, 5, 3]
"""
reduce():
"Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".

Unlike the previous two functions (Filter and Map), we have to import the reduce function from functools module using the statement:

from functools import reduce

We can also import the whole functools module by simply writing

Import functools

But in the case of bigger projects, it is not good practice to import a whole module because of time restraint.

SYNTAX:
reduce(function, iterable)
"""
# REDUCE FUNCTION
from functools import reduce

list_3 = [100, 200, 300, 400]
sum_list = reduce(lambda x, y: x + y, list_3)
print(sum_list)
# Example:
from functools import reduce

m = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(m)
# Output: 24
"""
Like the previous two, it also takes two-parameter. First one is the function and the second one is the iterable

Its working is very interesting as it takes the first two elements of the iterable and performs the function on them and converts them into a single element. 
It proceeds further, taking another element and performing the function of that one and the new element. For example, if we have four digits and the function 
wants to multiply them, then we can first multiply the first two and then multiply the third one in their resultant and then the forth and so on. 
The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, but it is not an iterator itself. 
It returns a single result.
"""

"""Python Lists And List Functions
Lists :
Python lists are containers used to store a list of values of any data type.
In simple words, we can say that a list is a collection of elements from any data type"""

list1 = ['Harry', 'Ram', 'Aakash', 'Shyam', 5000, 4.85]
print(list1)  # displays the list components
print(list1[0])  # displays the first component of the list
print(list1[1])  # displays the second component of the list
print(list1[2])  # displays the third component of the list
print(list1[3])  # displays the fourth component of the list
print(list1[4])  # displays the fifth component of the list
print(list1[5])  # displays the sixth component of the list

# The above list contains strings, an integer, and even an element of type float.
# A list can contain any kind of data i.e. it’s not mandatory to form a list of only one data type. The list can contain any kind of data in it.
# Note: If you put an index which isn’t in the list i.e. that index is not there in list then you will get an error.
# i.e. if a list named list1 contains 4 elements, list1[4] will throw an error because the list index starts from 0 and goes up to (index-1) or 3."""
"""List Slicing :
List slices, like string slices, returns a part of a list extracted out of it. 
Let me explain, you can use indices to get elements and create list slices as per the following format :"""
# seq = list1[start_index:stop_index]
"""List.append() : Add a single element to the end of the list
List.clear() : Removes all Items from the List
List.count() : returns count of the element in the list
List.extend() : adds iterable elements to the end of the list
List.index() : returns the index of the element in the list
List.insert() : insert an element to the list
List.pop() : Removes element at the given index
List.remove() : Removes item from the list
List.reverse() : reverses the list
List.sort() : sorts elements of a list """
"""  Just like we saw in strings, slicing will go from a start index to stop_index-1. 
It means the seq list which is a slice of list1 contains elements from the specified start_index to specified (stop_index – 1)."""
numbers = [23, 534, 65, 12, 45, 98, 45]
numbers.sort()  # sorts the list in ascending order
print(numbers)
numbers.reverse()  # sorts the list in descending order
print(numbers)
print(numbers[0:])  # displays the list till the end(default) from the given number
print(numbers[:5])  # displays the list from the starting(default) till the given number
print(numbers[::])  # displays the complete list
print(numbers[::-1])  # displays the reversed list
print(numbers[::2])  # displays the whole list with the gap of one character
print(len(numbers))  # displays the number of components in the list
print(max(numbers))  # displays the maximum number from the list
print(min(numbers))  # displays the minimum number from the list
numbers.append(7)  # adds this number to the list
print(numbers)
numbers.insert(1, 67)  # inserts 67 in the position 2 of the list
print(numbers)
numbers.pop()  # removes the last number from the list
print(numbers)
# Tuples in Python:
# Mutable : Can Change
# Immutable : Cannot Change
# A tuple is an immutable data type in Python. A tuple in python is a collection of elements enclosed in () (parentheses).
# Tuple once defined can’t be changed i.e. its elements or values can’t be altered or manipulated.
t1 = ()
print(type(t1))  # displays the data-type of t1 as tuple
tp = (1, 2, 3)  # here tp is a tuple and it cannot be formatted
print(tp)
"""Note: To create a tuple of one element it is necessary to put a comma  ‘,’ after that one element like this tup=(1,) 
because if we have only 1 element inside the parenthesis, the python interpreter will interpret it as a single entity which is why it’s important 
to use a ‘,’ after the element while creating tuples of a single element."""
a = 8
b = 5
a, b = b, a  # this is used to swap the values of two variables
print(a, b)
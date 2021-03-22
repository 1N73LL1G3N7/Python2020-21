"""Sets In Python
Let's start with the basic definition of sets in Mathematics.
People are already familiar with the concept of sets in mathematics know that as per the mathematical definition -
A set is a collection of well-defined objects and non-repetitive elements that is - a set with 1,2,3,4,3,4,5,2, 2, and 3 as its elements can be written as
{1,2,3,4,5}
No repetition of elements is allowed in sets.
In Python programming, sets are more or less the same. Let's look at the Python programming definition of sets:
“A set is a data structure, having unordered, unique, and un-indexed elements.
Elements in a set are also called entries and no two entries could be the same within a set.

Properties of sets in Python:
1. Sets are iterable (iterations can be performed using loops)
2. They are mutable (can be updated by adding or removing entries)
3. There is no duplication (two same entries do not occur)

Structure:
Elements of the sets are written in between two curly brackets and are separated with a comma, and in this simple way, we can create a set in Python.
The other way of forming a set is by using a built-in set constructor function.

Restrictions:
Everything has a limit to its functionality, there are some limitations on working with sets too.
1. Once a set is created, you can not change any of its items, although you can add new items or remove previous but updating an already existing item is not
possible.
2. There is no indexing in sets, so accessing an item in order or through a key is not possible, although we can ask the program if the specific keyword
we are looking for is present in the set by using “in” keyword or by looping through the set by using a for loop
Despite these restrictions, sets play a very important role in the life of a python programmer.
In most cases, these restrictions are never a problem for the programmer given he knows which data type to use when.
And this skill is something you will learn with time after writing a lot of python programs
Python has a set of built-in methods that you can use on sets.
Set Methods :
.add(): Adds an element to the set
.clear(): Removes all the elements from the set
.copy():	Returns a copy of the set
.difference():Returns a set containing the difference between two or more sets
.difference_update(): Removes the items in this set that are also included in another, specified set
.discard():Remove the specified item
.intersection(): Returns a set, that is the intersection of two other sets
.intersection_update(): Removes the items in this set that are not present in other, specified set(s)
.isdisjoint(): Returns whether two sets have a intersection or not
.issubset(): Returns whether another set contains this set or not
.issuperset(): Returns whether this set contains another set or not
.pop(): Removes an element from the set
.remove(): Removes the specified element
.symmetric_difference(): Returns a set with the symmetric differences of two sets
.symmetric_difference_update(): inserts the symmetric differences from this set and another
.union(): Return a set containing the union of sets
.update(): Update the set with the union of this set and others"""
set1 = set()
print(type(set1))  # displays the type of set1 as class set
set1_from_list = [1, 2, 3, 4, 5]
print(set1_from_list)  # displays the whole set
set1.add(6)  # adds element 6 to the set
set2 = set1.union({1, 2})  # unites the set to another set
print(set2, set1_from_list)
set2 = set2.intersection(set1_from_list)   # displays the common elements in both sets
print(set2)
print(set1.isdisjoint(set1_from_list))
set1_from_list.remove(2)
print(set1_from_list)

"""
Dictionary & Its Functions :Before going through the actual content i.e. the implementation of a dictionary,
it is important to know some basic theories so that we can know what we are going to learn and why we are spending our precious time learning it.
Let's start with the basic definition of a Python Dictionary:
“Python dictionary is an unordered collection of items. Each item of the dictionary has a key and value pair/ key-value pair.”
Now coming to the more formal approach:
Every programming language has its own distinct features, commonly known as its key features.
With that said, Python’s one out of the box feature is “dictionaries”.
Dictionaries may look very similar to a “List”, but dictionaries have some distinct features that do not hold true for other data types like lists,
and those features make it (python dictionary) special.
Here are a few important features of a python dictionary:
It is unordered (no sequence is required - data or entries have no order)
It is mutable (values can be changed even after its formation or new data/information can be added to the already existing dictionary,
we can also pop/remove an entry completely)
It is indexed (Dictionary contains key-value pairs and indexing is done with keys.
Also after the Python 3.7th update the compiler stores the entries in the order they are created)
No duplication of data (each key is unique; no two keys can have the same name so there is no chance for a data being over-repeated)
If we talk a little about how it works, its syntax comprises of key and values separated by colons in curly brackets,
where the key is used as a keyword, as we see in real life dictionaries, and the values are like the explanation of the key or what the key holds (the value).
And for the successful retrieval of the data, we must know the key, so that we can access its value just like in a regular oxford dictionary where
if we don't know the word or its spelling, we cannot obtain its definition.
Let's look into the syntax of a Python dictionary """
d1 = {}
print(type(d1))  # displays the data-type of d1 as dictionary
d2 = {"Ash": "Pizza", "Rohan": "Fish", "Subham": "Roti", "Aditya": {"B": "Maggie", "L": "Khichdi", "D": "Paratha"}}
print(d2)
# print(d2["Ash"])  # displays the pair with Ash
# print(d2["Aditya"]["B"])  # displays the pair with Aditya in B
# d2["Ankit"] = "Junk Food"  # adds Ankit to the dictionary
# print(d2)
# d2[420] = "Kebabs"
# del d2[420]  # deletes the component from the dictionary
# print(d2)
print(d2.copy())  # makes a copy of the dictionary
print(d2.get("Ash"))
d2.update({"Ash": "Burger"})  # updates the dictionary
print(d2)
print(d2.keys())  # displays all the keys
print(d2.items())  # displays all the items
"""With the help of dictionaries, we do not have to do most of our work manually through code like in C or C++. 
What I mean by this is that Python provides us with a long list of already defined methods for dictionaries that can help us to do our work in a shorter 
span of time with a very little amount of code. Some of these methods are, clear(), copy(), popitem(), etc. 
The best part about them is that no extra effort is required to be put in order to learn the functionality as their names explain their functions 
(in most of the cases), such as clear() will clear all the data from the dictionary, making it empty, copy() will make a copy of the dictionary, etc.
Some distinct features that a dictionary provides are:
We can store heterogeneous data into our dictionary i.e. numbers, strings, tuples, and the other objects can be stored in the same dictionary.
Different data types can be used in a single list, which can be made the value of some keys in the dictionary. etc."""

# Python Dictionary Methods :
"""Methods that are available with a dictionary are tabulated below. Some of them have already been used in the above examples.
dict.clear() : Removes all items from the dictionary
dict.copy() : Returns a shallow copy of the dictionary
dict.fromkeys(seq[, v]) : Returns a new dictionary with keys from seq and value equal to v (defaults to None)
dict.get(key[,d]) : Returns the value of the key. If the key does not exist, returns d (defaults to None)
dict.items() : Return a new object of the dictionary's items in (key, value) format
dict.keys() : Returns a new object of the dictionary's keys
dict.pop(key[,d]) : Removes the item with the key and returns its value or d if key is not found. 
                    If d is not provided and the key is not found, it raises KeyError
dict.popitem() : Removes and returns an arbitrary item (key, value).Raises KeyError if the dictionary is empty
dict.setdefault(key[,d]) : Returns the corresponding value if the key is in the dictionary.
                           If not, inserts the key with a value of d and returns d (defaults to None)
dict.update([other]) : Updates the dictionary with the key/value pairs from other, overwriting existing keys
dict.values() : Returns a new object of the dictionary's values """
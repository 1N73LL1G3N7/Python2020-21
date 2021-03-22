"""                                                            STRINGS
String is a data type in Python. Strings in Python programming language are arrays of bytes representing a sequence of characters.
In simple terms, Strings are the combination or collection of characters enclosed in quotes.
Primarily, you will find 3 types of strings in Python :
Single Quote String – (‘Single Quote String’)
Double Quote String – (“Double Quote String”)
Triple Quote String – (‘’’ Triple Quote String ‘’’)
Let us now look into some functions you will use to manipulate or perform operations on strings."""
mystr = "Ashish is learning Python."
"""len() Function : This len() function returns the total no. of characters in a string.
E.g. for string a="abc", len(a) will return 3 as the output as it is a string variable containing 3 characters"""
print(len(mystr))  # displays the number of CHARACTERS in mystr
"""
Strings are one of the most used data types in any programming language because most of the real-world data such as name, address,
or any sequence which contains alphanumeric characters are mostly of type ‘String’.
String Slicing :
As we know the meaning of the word ‘slice’ is ‘a part of’. I am sure you have sliced paneer cubes at home!
Just like paneer slice refers to the part of the paneer cube; In Python, the term ‘string slice’ refers to a part of the string,
where strings are sliced using a range of indices.
To do string slicing we just need to put the name of the string followed by [n:m].
It means ‘n’ denotes the index from which slicing should start and ‘m’ denotes the index at which slicing should terminate or complete.
Let's look into an example!"""
print(mystr[0:6])  # displays characters from position 0 to 6 i.e. Ashish
print(mystr[0:18])  # displays 3 words according to their position
# print(mystr[0:100]  this displays error as there are no 100 character
"""In Python, string slicing s[n:m] for a string s is done as characters of s from n to m-1. It means characters are taken from the first index to second index-1.
For E.g. abc="Demo" then abc[0:3] will give ‘Dem’ and will not give ‘Demo’ coz index number of ‘D’ is 0, ‘e’ is 1, ‘m’ is 2, and ‘o’ is 3.
So it will give a range from n to m-1 i.e. 0 to 3-1=2. That’s why we got output ‘Dem’.
In string slicing, we sometimes need to give a skip value i.e. string[n:m:skip_value]. This simply takes every skip_value the character.
By default, the skip value is 1 but if we want to choose alternate characters of a string then we can give it as 2.
We can display negative values also as the position of the characters in the string. Last character is positioned as -1 previous one as -2 and so on"""
print(mystr[0:26:2])  # displays the whole string with a gap of 1 characters in between
print(mystr[0:])  # displays the whole string from 0 position till end(default)
print(mystr[:6])  # displays the string from the starting(default 0) till given position
print(mystr[::])  # displays whole string without giving a gap
print(mystr[::5559])  # displays the starting character and then gives the gap of given character, here 5559; here nothing is there after 5559 steps thus nothing is displayed
print(mystr[::-1])  # displays the whole string in reversed order; if there is -2 in place of -1,then the string will be displayed in reversed order with a gap of 1 character and so on..
mystr2 = 'ashish giri'
print(type(mystr2))  # displays the type of variable
print(mystr2.isalnum())  # displays true if the variable is numeric(whitespace should not be there) or else displays false.
print(mystr2.isalpha())  # displays true if the variable is alpha-numeric(whitespace should not be there) or else displays false.
#  Some of the most used string functions :
# string.endswith(): This function allows the user to check whether a given string ends with passed argument or not. It returns True or False.
print(mystr2.endswith("giri"))
# string.count(): This function counts the total no. of occurrence of any character in the string.
# It takes the character whose occurrence you want to find as an argument.
print(mystr2.count("i"))
# string.capitalize(): This function capitalizes the first character of any string. It does not take any argument.
print(mystr2.capitalize())
# string.upper(): It returns the copy of the string converted to the uppercase.
print(mystr2.upper())
# string.lower(): It returns the copy of the string converted to lower case.
print(mystr2.lower())
# string.find(): This function finds any given character or word in the entire string. It returns the index of first character from that word.
print(mystr2.find("giri"))
# string.replace(“old_word”, “new_word”): This function replaces the old word or character with a new word or character from the entire string.
print(mystr2.replace("giri", "goswami"))

"""F-Strings & String Formatting In Python

String formatting is used to design the string using formatting techniques provided by the particular programming language. 
From the % formatting to the format() method, to format string literals, there is no limit as to the potential of string crafting. 
There are four significant ways to do string formatting in Python. In this tutorial, we will learn about the four main approaches to string formatting in 
Python.

#1 String Formatting (% Operator)
Python has a built-in operation that we can access with the % operator. This will help us to do simple positional formatting. If anyone knows a little bit about C programming, then they have worked with printf statement, which is used to print the output. This statement uses the % operator. Similarly, in Python, we can perform string formatting using the % operator. For Example:

name="Jack”
n="%s My name is %s” %name
print(n)

Output: "My name is Jack."

The problem with this method is when we have to deal with large strings. If we specify the wrong type of input type operator, then it will throw an error. 
For Example, %d will throw a TypeError if the input is not an integer.

#2 Using Tuple ()
The string formatting syntax, which uses % operator changes slightly if we want to make multiple substitutions in a single string. 
The % operator takes only one argument, to mention more than one argument, use tuples. Tuples are better than using the old formatting string method. 
However, it is not an ideal way to deal with large strings. For Example:

name=”Jack”
class=5
s=”%s is in class %d”%(name,class)
print(s)

Output: Jack is in class 5.

#3  String Formatting (str.format)
Python 3 introduced a new way to do string formatting. format() string formatting method eliminates the %-operator special syntax and makes the syntax for 
string formatting more regular. str.format() allows multiple substitutions and value formatting. We can use format() to do simple positional formatting, 
just like you could with old-style formatting:
In str.format(), we put one or more replacement fields and placeholders defined by a pair of curly braces { } into a string.

Syntax: {}.format(values)

For Example,

str = "This article is written in {} "
print (str.format("Python"))

Output: This article is written in Python.

This string formatting method is preferred over %-style formatting. Using the format() method, we can deal with large strings, 
and the code will become more readable.

#4 Using f-Strings ( f ):
Python added a new string formatting approach called formatted string literals or "f-strings." This is a new way of formatting strings. 
A much more simple and intuitive solution is the use of Formatted string literals.f-string has an easy syntax as compared to previous string formatting 
techniques of Python. They are indicated by an "f" before the first quotation mark of a string. Put the expression inside { } to evaluate the result. 
Here is a simple example

# declaring variables

str1="Python”

str2="Programming”

print(f"Welcome to our {str1}{str2} tutorial”)
Output: Welcome to our Python Programming tutorial.
"""
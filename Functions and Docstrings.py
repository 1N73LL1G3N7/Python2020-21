"""Functions And Docstrings
“Functions in Python can be defined as lines of codes that are built to create a specific task and can be used again
and again in a program when called.”
There are two types of functions in the Python language:
1. Built-in functions
2. User-defined functions
The advantages of using a function:
If we are working on a big project then we will prefer to make as many functions as possible, so every other member
of our team could use that.
By using functions, we can avoid the repetition of code to an extent. More lines of code mean less efficiency.
Also repeating the same code at different places will just make the code more crowded than required.
The re-usability of code is ensured by using functions. We can even use a function inside another function or
in any part of our code.
By making a function of code that we are going to use again and again, we can save a lot of time."""


def average_calc(a, b):
    """This is a function which will calculate average of two numbers"""
    average = (a + b) / 2
    return average


print(average_calc.__doc__)

avg = (average_calc(84, 1084))
print("The average is", avg)

""" Docstrings
Docstring is a short form of documentation string. Its purpose is to give the programmer a brief knowledge about the 
functionality of the function. It must be the first string in a function, and it is also an optional string but always 
good to have it while working on programs having multiple functions. The syntax for writing a docstring is very simple 
as it is just a string written in between three double quotes placed three times (""" """) on either side of the string.
But it has to be the first line of code in the function’s body. To call a docstring we write the name of the function 
followed by ._doc_."""

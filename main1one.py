"""
Using if __name__ == “__main__” statement is one such concept that may be difficult to grasp for beginners, but once learned, it is very helpful and used
quite often afterward. A module is just a file containing a python code with a .py extension and can be imported to other files.
That's where the keyword __name__ comes in. Let’s understand __name__ first before moving onto if __name__ == “__main__.

What is __name__?
“A __name__ is a built-in variable that returns us the name of the module being used.”
In simple words, by using __name__, we can check whether our module is being imported or run directly.

Working with Python files, when we import one file to another, along with the functions and variables, we also import all the print statements and other such
data that we do not require. In such cases, we insert all the data of the module that we do not want others to import into the main, and thus it can only be
executed by the file containing the main only.

The main is a point of the program from where the program starts its execution.
Every program has its own main function. The main function can only be executed when it is being run in the same program.
If the file is being imported, then it is no longer the main function because the file that is importing it has its own “main” function.

The syntax is :
if__name__=="__main__":
    # Logic Statement

What are the Advantages of using if __name__ == “__main__” statement?
Following are the advantages of using if __name__ == “__main__” statement:
Using the main in our file, we can restrict some data from exporting to other files when imported.
We can restrict the unnecessary data, thus making the output cleaner and more readable.
We can choose what others may import or what they may not while using our module.
Modules in Python has a special attribute called __name__. The value of the __name__ attribute is set to __main__ when the module is run as the main program.
Otherwise, the value of __name__ is set to the name of the module. The if __name__ == “__main__” block prevents the certain code from being run when the module
is imported.
"""


def speak_dialogue(dialogue):
    return f"Ye {dialogue} Ashish ko de de Thakur !"


def add_int(num1, num2):
    return num1 + num2


print("Imported from", __name__)
if __name__ == '__main__':
    print(speak_dialogue("Haath"))
    print(add_int(6, 9))

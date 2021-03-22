"""
In Python programming, there are two types of arguments that can be passed in a function.
1. positional arguments
2. keyword arguments
Positional arguments are the one in which an order has to be followed while passing arguments. We have been dealing with them until now.
We know how normal functions work with positional arguments, so now we will directly start exploring keyword arguments.
But to understand them, we have to know about asterisk or more commonly known in Perl 6 and ruby as a splat operator.
Asterisk is used in python as a mathematical symbol for multiplication, but in case of arguments, it refers to unpacking. The unpacking could be for a list,
tuple, or a dictionary. We will discover more about it by defining *args and **kwargs.
*args:
args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple.
Suppose that we have to enter the name of students who attended a particular lecture. Each day the number of students is different, so positional arguments
would not be helpful because we can not leave an argument empty in that case. So the best way to deal with such programs is to define the function using the
class name as formal positional argument and student names with parameter *args. In this way, we can pass student's names using a tuple.
Note that the name args does not make any difference, we can use any other name, such as *any_name. The only thing that makes a difference is the Asterisk(*).
**kwargs:
The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary. Let's take the same example we used in the
case of *args. The only difference now is that the student's registration, along with the student's name, has to be entered. So what **kwargs does is, it
sends argument in the form of key and value pair. So the student's name and their registration both can be sent as a parameter using a single ** kwargs
statement.
Same as we discussed for args*, the name kwargs does not matter. We can write any other name in its place, such as **attendance.
The only mandatory thing is the double asterisks we placed before the name.   """


def func_args_kwargs(*students, **heroes):
    for students in students:
        print(students)
    for key, values in heroes.items():
        print(f"{key} is the {values}")


Class9 = ["Ashish", "Amit", "Abhijeet", "Kishan", "Dhruv"]
func_args_kwargs(*Class9)

tasks = {"Ashish": "Yellow-house Captain", "Amit": "Red-house Captain", "Abhijeet": "Blue-house Captain", "Kishan": "Singer", "Dhruv": "Green-house Captain"}
func_args_kwargs(**tasks)

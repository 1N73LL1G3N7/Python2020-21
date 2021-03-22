"""Loops and Why do we use loops?
Complex problems can be simplified using loops
Less amount of code required for our program
Lesser code so lesser chance or error
Saves a lot of time
Can write code that is practically impossible to be written
Programs that require too many iterations such as searching and sorting algorithms can be simplified using loops
How to write a for loop?
For loop basically depends upon the elements it has to iterate instead of the statement being true or false.
In different programming languages the way to write a loop is different, in java and C it could be a little technical and difficult to grasp for a beginner
but in Python, its simple and easy.
Advantages of loops:
The re-usability of code is ensured
We do not have to repeat the code again and again, just have to write it one time
We can transverse through data structures like list, dictionary, and tuple
We apply most of the finding algorithms through loops"""
# For Loops
# The for loop is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object.
"""For Loops In Python
Starting with the technical definition of for loops:
For loop is also just a programming function that iterates a statement or a number of statements based on specific boundaries under certain defined conditions, 
that are the basis of the loop.
Note that the statement that the loop iterates must be present inside the body of the loop.
Regarding loops, iteration means going through some chunk of code again and again. 
In programing it has the same meaning, the only difference is that the iteration depends upon certain conditions and upon its fulfillment, the iteration stops,
and the compiler moves forward."""

list1 = [["Ash", 3], ["Brock", 2], ["Max", 5], ["Clemont", 6]]
for item, lollipop in list1:
    print(item, "eats", lollipop, "lollipops")

# QUIZ
OneDigitNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for digit in OneDigitNums:
    if str(digit).isnumeric() and digit == 6:
        print("6 is a one digit number")
# While Loops
# The while statement is used for repeated execution as long as an expression is true.
"""While Loops In Python
“A while loop in python runs a bunch of code or statements again and again until the given condition is true when the condition becomes false, 
the loop terminates its repetition.”
The syntax for while loop is simple and very much like for loop. We have to use the keyword “while”, along with it we have to put a condition in 
parenthesis and after that, a colon is placed. The condition could be either true or false. Until the condition is true, the loop will keep on executing 
again and again. If we use a certain sort of condition in our while loop that, it never becomes false then the program will keep on running endlessly, 
until we stop it by force. So, this kind of mistake in our syntax is known as logical/human error.
To terminate an infinite loop, you can press Ctrl+C on your system.
A “for” statement loop runs until the iteration through, set, lists, tuple, etc. or a generator function is completed. 
In case of while loop the statement simply loops until the condition, we have provided becomes false. 
We generally use for loops for areas where we are already familiar with the number of iterations and use while loop where the number of iterations are unknown. 
Because while loop is solely based on the state of its condition.
For a While loop to run endlessly we can pass true or 1 as a condition.
1 is also used in place of writing true as a whole. So, in this case, the condition will never become false so the program will run endlessly. 
But these kinds of programs do not output anything because they could never complete their execution."""
i = 1
while i <= 100:
    print(i)
    i += 1

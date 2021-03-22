import random
import wikipedia
import pendulum
"""
Using Python External & Built In Modules
In Python, a module can be defined as a file containing a runnable python code. The extension used by modules in Python is .py.
Hence any simple file containing Python code can be considered as a module if its extension is .py. The file and module names are the same;
hence we can call a module only by name without using the extension. Along with this, a module can define functions, classes, and variables.
There are two types of modules.
1. Built-in
2. External
Built-in Modules:
Built-in modules are already installed in Python by default. We can import a module in Python by using the import statement along with the specific module name.
We can also access the built-in module files and can read the Python code present in them. Newly integrated modules are added in Python with each update.
Some important modules names are as follows
calendar :
used in case we are working with calendars

random :
used for generating random numbers within certain defined limits

enum :
used while working with enumeration class

html :
for handling and manipulating code in HTML

math :
for working with math functions such as sin, cos, etc.

runpy :
runpy is an important module as it locates and runs python modules without importing them first

External modules:
External modules have to be downloaded externally; they are not already present like the built-in ones. Installing them is a rather easy task and can be
done by using the command “pip install module_name” in the compiler terminal. Being familiar with all the modules seems like a long shot for even the best
of programmers because there are so many modules available out there. So, we can search and find modules according to our needs and use them as there is no
need to remember all of them when we can simply look for them on the internet when the need occurs.
Being programmers, module makes our life a lot easy. Unlike programming languages in the past, also known as low-level programming languages,
Python provides us with a lot of modules that make our coding much easy because we do not have to write all the code ourselves.
We can directly access a module for a specific task. For example, to generate a random number within two numbers, known as its limit,
we do not have to write a function ourselves with loops and a large number of lines of codes. Instead, we can directly import a module,
and this makes our work simple.
We should not concern ourselves with the code written inside the module; instead, we can search the internet for the functions and properties.
If we are not satisfied with the available module's work or could not find a module that could help us in the required manner, we can create our own module
by making a file with .py extension. The module file will be like any other file you see in Python, the difference will just arise in the extension."""

# Using Random module

random_number = random.randint(0, 10)  # Generates a random integer in between 0 and 10 including 0 and 10.
print(random_number)

random_number2 = random.random() * 100  # Generates a random float number till 100 from 0.
print(random_number2)

dice_number = [1, 2, 3, 4, 5, 6]
my_choice = random.choice(dice_number)  # Generates a random element from the list
print(my_choice)

# Using Wikipedia module
summary = wikipedia.summary("Wikipedia")  # Generates a summary
print(summary)

search = wikipedia.search("Narendra Modi")  # Provides the search results
print(search)

Ind = wikipedia.page("india")  # Connects with the wikipedia page
var1 = Ind.title
var2 = Ind.url
var3 = Ind.content
var4 = Ind.links[0:10]
print("Title :", var1, "\nUrl :", var2, "\nContent :", var3, "\nExternal Links :", var4)

# Using Pendulum module
now = pendulum.now()
print(now)

future = now.add(days=1, weeks=1, hours=1)  # adds the current time as per the instructions
past = now.subtract(weeks=1)  # subtracts from the current time
print("Future :", future, "\nPast :", past)

birthday = pendulum.date(2006, 7, 12)  # Selects this date
my_age = birthday.age
print(my_age)

today = pendulum.today()
tomorrow = pendulum.tomorrow()
yesterday = pendulum.yesterday()
print("Today :", today, "\nTomorrow :", tomorrow, "\nYesterday :", yesterday)

wish_birthday = birthday.is_birthday(today)
print(wish_birthday)

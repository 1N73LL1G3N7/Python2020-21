# File IO Basics
"""
How to open a file?
Python has a built-in open() function to open a file.
The syntax of the function is:
open("filename" ,"mode")
To open a file, we must specify two things,
1. Name of the file and its extension
2. Access mode where we can specify in which mode file has to be opened, it could either be read (r), write (w) or append(a), etc. For more information
regarding access modes, refer to the previous tutorial.
The open function returns a file object. We store this file object into a variable which is generally called as a file pointer/file handler.
You can use file pointer to further add modifications in the file. An error could also be raised if the operation fails while opening the file.
It could be due to various reasons like trying to access a file that is already closed or trying to read a file open in write mode.
How to read a file?
To read a file in Python, there are various methods available,
We can read a whole file line by line using a for loop in combination with an iterator. This will be a fast and efficient way of reading data.
When opening a file for reading, Python needs to know exactly how the file should be opened. Two access modes are available reading (r), and reading in
binary mode (rb). They have to be specified during opening a file with the built-in open() method.
The read() method reads the whole file by default. We can also use the read(size) method where you can specify how many characters we want to return i.e.
f.read(2); # Here, you will get the first two characters of the file.
You can use the readline() method to read individual lines of a file. By calling readline() a second time, you will get the next line.
readlines() method reads until the end the file ends and returns a list of lines of the entire file. It does not read more than one line.
f.readlines() # Returns a list object
Note: The default mode to read data is text mode. If you want to read data in binary format, use ''rb".
Is it necessary to close a file?
The answer is yes, it is always the best practice to close a file after you are done performing operations on it.
However, Python runs a garbage collector to clean up the unused objects, but as good programmers, we must not rely on it to close the file.
Python has a build-in close() function to close a file i.e;
f.close()

Note: f is an object for the file. It is not a method or a special character.
"r" - Opens file for reading(default)
"w" - Opens file for writing
"x" - Creates file if it doesn't exists
"a" - Add more content to the file
"t" - text mode(default)
"b" - binary mode
"+" - read and write mode
“w” mode:
Here “w” stands for write. After opening or creating a file, a function, f.write() is used to insert text into the file.
The text is written inside closed parenthesis surrounded by double quotations. There is a certain limitation to the write mode of the opening file that it
overrides the existing data into the file. For a newly created file, it does no harm, but in case of already existing files, the previous data is lost as
f.write() overrides it.
“a” mode:
“a” symbolizes append mode here. In English, appends mean adding something at the end of an already written document, and the same is the function the mode
performs here. Unlike write mode, when we use "a" keyword, it adds more content at the end of the existing content. The same function i.e., f.write() is used
to add text to the file in append mode. It is worth noting that append mode will also create a new file if the file with the same name does not exist and can
also be used to write in an empty file.
“r+” mode:
r+ mode is more of a combination of reading and append than read and write. By opening a file in this mode, we can print the existing content on to the
screen by printing f.read() function and adding or appending text to it using f.write() function
"""
f = open("File IO Basics.txt")
# displaying the content of the file
# f = open("File IO Basics.txt", "r")
content = f.read()
print(content)
# this also can be used
for line in f:
    print(line, end="")
# displaying only one line, if multiple lines are needed, repeat this code
content = f.readline()
print(content)
# displaying a list of the lines
content = f.readlines()
print(content)
# writing and appending
# f = open("File IO Basics.txt", "w")
# f = open("File IO Basics.txt", "a")
a = f.write("Ashish")  # this is used to write a file
print(a)
# handling read and write both
# f = open("File IO Basics.txt", "r+")
f = open("harry2.txt", "r+")
print(f.read())
f.write("thank you")
# Seek and Tell
print(f.tell())  # tells the position of the pointer
print(f.readline())
print(f.tell())  # gets updated now and increases it's value
print(f.readline())
print(f.seek(0))  # places the pointer to the given argument position
print(f.readline())
f.close()
# Using with block to access files
with open("File IO Basics.txt") as f:
    a = f.readline(10)
    print(a)
# no need to even close the file

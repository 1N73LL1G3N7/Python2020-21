# A variable is a name given to any storage area or memory location in a program.
# It acts like a container that contains some information
a = 34  # Variable storing an integer value.
b = 23.2  # Variable storing a float value.
c = "hello"  # Variable storing a sting value.
d = True  # Variable storing a boolean value.
'''                          Rules for defining a variable in python :
A variable name can contain alphabets, digits and underscores(_).
A variable name can only start with an alphabet and underscore.
It can't start with a digit.
No whitespaces are allowed inside a variable name
Also reserved keywords are not recommended to be used as variable name. 
                                       type() function :
type() function is a function that allows a user to find data type of any variable. 
It returns the data type of any data contained in the variable passed to it.'''

var1 = 100
print(type(var1))  # This displays the datatype of var1 as integer.
var2 = 23.9
print(type(var2))  # This displays the datatype of var2 as float.
var3 = "ashish"
print(type(var3))  # This displays the datatype of var3 as string.
var4 = False
print(type(var4))  # This displays the datatype of var4 as boolean.

# Note – We can't do arithmetic operations of numbers with strings i.e. we can't add a string to any number.
# We can add (concatenate) two or more strings and the strings will be concatenated to return another string.
'''                                           Typecasting  
Typecasting is the way to change one data type of any data or variable to another datatype,
i.e. it changes the data type of any variable to some other data type.
There are many functions to convert one data type into another type :
str() – this function allows us to convert some other data type into a string.
int() – this function allows us to convert some other data type into an integer. For example, str("34") returns 34 which is of type integer (int)
float() – this function allows us to convert some other data type into floating-point number i.e. a number with decimals.   '''
'''                                      input() Function :
This function allows the user to receive input from the keyboard into the program as a string. 
input() function always takes input as a string i.e. if we ask the user to take a number as input 
even then it will take it as a string and we will have to typecast it into another data type as per the use case.'''

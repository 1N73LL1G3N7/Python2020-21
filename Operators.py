# Operators in Python
"""“Operators in Python can be defined as symbols that assist us to perform certain operations.
The operations can be between variable and variable, variable and value, value and value”
Operators that Python Language supports are:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""
# ARITHMETIC OPERATORS
"""Basic mathematical operations such as addition, multiplication, subtraction, division, etc. are performed with the help of arithmetic Operations. 
It contains nearly all operations that we can perform with the help of a calculator. Symbols for such operators include *, /, %, -, //, etc.
"""
print('Arithmetic Operators')
print("5 + 3 is", 5 + 3)  # Add two operands x + y
print("5 - 3 is", 5 - 3)  # Subtract right operand from the left x - y
print("5 * 3 is", 5 * 3)  # Multiply two operands x * y
print("5 / 3 is", 5 / 3)  # Divide left operand by the right one (always results into float) x / y
print("5 // 3 is", 5 // 3)  # Floor division - division that results into whole number adjusted to the left in the number line x // y
print("5 ** 3 is", 5 ** 3)  # Exponent - left operand raised to the power of right x**y (x to the power y)
print("5 % 3 is", 5 % 3)  # Modulus: remainder of the division of left operand by the right x % y (remainder of x/y)

# ASSIGNMENT OPERATORS
"""The assignment operator is used to assign values to a variable. In some cases, we have to assign a variable’s value to another variable, 
in such cases the value of the right operand is assigned to the left operand. One of the basic signs from which we can recognize an assignment operator 
is that it must have an equal-to(=) sign. Some commonly used assignment operators include +=, -=, /=, etc.
"""
print('Assignment Operators')
x = 5  # assign
print(x)
x += 7  # add-assign
print(x)
x -= 3  # subtract-assign
print(x)
x *= 2  # multiply-assign
print(x)
x /= 6  # divide-assign

# COMPARISON OPERATORS
"""They are also known as relational operators. They compare the values on either side of the operator and decide the relation among them.
Commonly used comparison operators include ==, >, < , >=,etc.
"""
print('Comparison Operators')
x = 10
y = 12
print(x > y)  # Greater than - True if left operand is greater than the right
print(x < y)  # Less than - True if left operand is less than the right
print(x == y)  # Equal to - True if both operands are equal
print(x != y)  # Not equal to - True if operands are not equal
print(x >= y)  # Greater than or equal to - True if left operand is greater than or equal to the right
print(x <= y)  # Less than or equal to - True if left operand is less than or equal to the right

# LOGICAL OPERATORS
"""Logical operators perform logical AND, OR and NOT, operations. They are usually used in conditional statements to join multiple conditions.
AND, OR and NOT keywords are used to perform logical operations.
"""
print('Logical Operators')
x = True
y = False
print('x and y is', x and y)  # True if both the operands are true
print('x or y is', x or y)  # True if either of the operands is true
print('not x is', not x)  # True if operand is false (complements the operand)

# IDENTITY OPERATORS
"""Identity operator checks if two operands share the same identity or not, which means that they share the same location in memory or different. “is” and 
“is not” are the keywords used for identity operands.
"""
print('Identity Operators')
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 5]
print(x1 is y1)  # True if the operands are identical (refer to the same object)
print(x2 is not y2)  # True if the operands are not identical (do not refer to the same object)
print(x3 is y3)

# MEMBERSHIP OPERATORS
"""Membership operand checks if the value or variable is a part of a sequence or not. The sequence could be string, list, tuple, etc. “in” and “not in” are 
keywords used for membership operands.
"""
print('Membership Operators')
x = 'Hello world'
y = {1: 'a', 2: 'b'}
print('H' in x)  # True if value/variable is found in the sequence
print('hello' in x)
print(1 not in y)  # True if value/variable is not found in the sequence

# BITWISE OPERATORS :
"""Bitwise operands are used to perform bit by bit operation on binary numbers. 
First, we have to change the format of the number from decimal to binary and then compare them using AND, OR, XOR, NOT, etc.
To understand bitwise fully, we must have the basic knowledge of the conversion of decimal into binary. 
For example, the binary for the first five number is:
0001
0010
0011
0100
0101
And so on."""
# &
# Bitwise AND
# |
# Bitwise OR
# ~
# Bitwise NOT
# ^
# Bitwise XOR
# >>
# Bitwise right shift
# <<
# Bitwise left shift

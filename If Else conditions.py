"""
If Else & Elif Conditionals In Python
“If, else and elif statement can be defined as a multiway decision taken by our program due to the certain conditions in our code.”
“If and else” are known as decision-making statements for our program.
They are very similar to the decision making we apply in our everyday life that depends on certain conditions.
Our compiler will execute the if statement to check whether it is true or false now if it’s true the compiler will execute the code in the
“if” section of the program and skip the bunch of code written in “elif” and “else”. But if the “if” condition is false then the compiler will
move towards the elif section and keep on running the code until it finds a true statement(there could be multiple elif statements).
If this does not happen then it will execute the code written in the “else” part of the program.
An “if” statement is a must because without an if we cannot apply “else” or “else-if” statement.
On the other hand else or else if statement are not necessary because if we have to check between only two conditions we use only “if and else” and
even though if we require code to run only when the statement returns true and do nothing if it returns false then an else statement is not required at all.
Some technical issues related to the working of decision statements:
There is no limit to the number of conditions that we could use in our program.
We can apply as many elif statements as we want but we can only use one “else” and one “if” statement.
We can use nested if statements i.e. if statement within an if statement. It is quite helpful in many cases."""
var1 = 100
var2 = int(input("Enter an integer :\n"))
if var2 > var1:
    print("Entered integer is Greater")
elif var2 == var1:
    print("Entered integer is Equal")
else:
    print("Entered integer is Lesser")
"""Decision statements can be written using logical conditions which are:
Equal to
Not equal to
Less than
Greater than
Greater than equal to
Less than equal to
We can also use Boolean or our custom-made conditions too.
"""
list1 = [1, 2, 3, 4, 5]
print(5 not in list1)
if 5 in list1:
    print("5 is in the list")

# QUIZ
age = int(input("Enter your age :\n"))
if age > 18:
    print("You can drive.")

elif age == 18:
    print("Driving Test Required.")

elif age > 100:
    print("Do not fool me...")

else:
    print("Travel with your feet, kid.")

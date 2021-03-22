# Exercise 4 - PATTERN PRINTING
print("Enter the number of rows of stars you want to print :")
num1 = int(input())
print("Enter 1 if you want it to be printed in ascending order and Enter 0 if you want it in descending order :")
x = int(input())
num2 = bool(x)
if num2:
    for i in range(1, num1 + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif not num2:
    for i in range(num1, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

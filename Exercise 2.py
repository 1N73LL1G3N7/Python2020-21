# Create a faulty calculator that shows incorrect answers for 45 * 3, 56 + 9, and 56 / 6

operator = (input("Enter the operator you want to use :\n"))
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 == 45 and num2 == 3 and operator == "*":
    print("The answer is 555")
elif num1 == 56 and num2 == 9 and operator == "+":
    print("The answer is 77")
elif num1 == 56 and num2 == 6 and operator == "/":
    print("The answer is 4")
elif operator == "+":
    print("The answer is ", num1 + num2)
elif operator == "-":
    print("The answer is ", num1 - num2)
elif operator == "*":
    print("The answer is ", num1 * num2)
elif operator == "/":
    print("The answer is ", num1 / num2)
else:
    print("Invalid Input...")

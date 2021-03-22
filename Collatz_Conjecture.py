# COLLATZ CONJECTURE


def collatz(x):
    """
        :param x: Whole number
        :return: f(x) = { 3x + 1  # if x is odd
                        { x / 2  # if x is even
    """
    if x % 2 == 0:
        return x // 2
    elif x % 2 == 1:
        return 3 * x + 1
    else:
        return None


x = int(input("Enter any whole number to get the Collatz Conjecture sequence :\n"))

try:
    print("The Collatz Sequence is :")
    print(x)
    while x != 1:
        x = collatz(x)
        print(x)
except ValueError:
    print("ERROR : INVALID INPUT, Please input a whole number...")

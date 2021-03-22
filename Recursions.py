"""Recursion occurs when a function calls itself."
Mostly both recursion and iteration are used in association with loops, but both are very different from each other. In both recursion and iteration,
the goal is to execute a statement again and again until a specific condition is fulfilled. An iterative loop ends when it has reached the end of its
sequence; for example, if we are moving through a list, then the loop will stop executing when it reached the end of the list. But in the case of recursion,
the function stops terminating when a base condition is satisfied.
Recursion:
There are two essential and significant parts of a recursive function. The first one is the base case, and the second one is the recursive case.
In the base case, a conditional statement is written, which the program executes at the end, just before returning values to the users.
In the recursive case, the formula or logic the function is based upon is written.
A recursive function terminates to get closer to its base case or base condition.
As in case of loops, if the condition does not satisfy the loop could run endlessly, the same is in recursion that if the base case is not met in the call,
the function will repeatedly run, causing the system to crash.
In case of recursion, each recursive call is stored into a stack until it reaches the base condition, then the stack will one by one return the calls
printing a series or sequence of numbers onto the screen. It is worth noting that stack is a LIFO data structure i.e., last in first out.
This means that the call that is sent into the stack at the end will be executed first, and the first one that was inserted into the stack will be executed
at last.
Iteration:
We have a basic idea about iteration as we have already discussed it in tutorial # 16 and 17 relating loops.
Iteration runs a block of code again and again, depending on a user-defined condition. Many of the functions that recursion performs can also be achieved
by using iterations but not all, and vice versa.

Recursion vs. Iteration:
Recursion can only be applied to a function, while iteration can be used for any number of lines of code, we want to repeat
Lesser coding has to be done in case of recursion than iteration
Back tracing or reverse engineering in case of recursion can be difficult.
In the case of recursion, if the condition is not met, the system will repeat a few times and then crash while in case of iteration it will continue to run endlessly.
Even though less coding has to be written in case of recursion, it is still slower in execution because the function has to be called again, and again, storing data into the stack also increases the time of execution."""

# n! = n * n - 1 * n - 2 * n - 3 * ...... 1
# n! = n * (n - 1)!


def factorial_recursive_method(n):
    """
        :param n: Integer
        :return: n * n - 1 * n - 2 * n - 3 * ...... 1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive_method(n - 1)


number2 = int(input("Enter the number of which you want the factorial(Recursive approach) : "))
print(factorial_recursive_method(number2))


def factorial_iterative_method(m):
    """
        :param m: Integer
        :return: m * m - 1 * m - 2 * m - 3 * ...... 1
    """
    fac = 1
    for i in range(m):
        fac = fac * (i + 1)
    return fac


number1 = int(input("Enter the number you want to get factorial of(Iterative approach) : "))
print(factorial_iterative_method(number1))
# QUIZ
# Printing Fibonacci Sequence


def fibonacci_sequence(a):
    """
        :param a: Integer
        :return: 0, 1, 1, 2, 3, 5, 8, 13 ....
    """
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fibonacci_sequence(a - 1) + fibonacci_sequence(a - 2)


number3 = int(input("Enter the position of the number in fibonacci sequence to get the number : "))
print(fibonacci_sequence(number3))

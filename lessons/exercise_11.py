# Calculate Factorial (Without Recursion): Write a function to calculate the factorial of a given positive integer without using recursion.
# A factorial is a mathematical operation that involves multiplying a positive integer by all the positive integers smaller than itself down to 1. 
# It's represented using the exclamation mark (!). For example, the factorial of a positive integer n is denoted as n! and is calculated as:

def factorial(n):
    # Code here
    return 0


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

print(factorial(0))
assert(factorial(0) == 1) #???

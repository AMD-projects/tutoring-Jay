def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print(result)

# ex: fib seq. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# n = (n-1) + (n-2)

def fib_seq(n):
    if n <= 1:
        return n
    else:
        return(fib_seq(n-1) + fib_seq(n-2))
    
print(fib_seq(0))
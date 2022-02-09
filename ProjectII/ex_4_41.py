from misc_functions import *

"""
Returns the nth number of the fibonacci sequence using recursion
"""
def recursive_fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


"""
Returns the nth number of the fibonacci sequence
"""
def fibonacci(n):
    a = 1
    b = 1
    for _ in range(2, n):
        temp = a + b
        a = b
        b = temp
    return b


if __name__ == "__main__":
    n = fibonacci(104911)
    if miller_rabin(n, 5):
        print("The integer " + str(n) + " is a strong probable prime")
    else:
        print("The integer " + str(n) + " is not a strong probable prime")

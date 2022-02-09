from math import e
from math import sqrt
from numpy import log


def findDivisorSum(n):
    sum = n + 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            sum += n//i
    return sum


if __name__ == "__main__":
    for n in range(2, pow(10, 7)):
        div_sum = findDivisorSum(n)
        if div_sum > pow(e, 0.578) * n * log(log(n)):
            print(n)

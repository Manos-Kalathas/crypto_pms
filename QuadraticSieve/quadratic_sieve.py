from misc_functions import *
import random
from math import sqrt
from math import log
from math import exp
from decimal import *


"""
Calculates the legendre symbol of a and m
https://en.wikipedia.org/wiki/Legendre_symbol
"""
def legendre(a, m):
    a = a % m
    t = 1
    while a != 0:
        while (a % 2 == 0):
            a /= 2
            if (m % 8) >= 3 and (m % 8) <= 5:
                t = -t
        a, m = m, a
        if congruent(a, 3, 4) and congruent(m, 3, 4):
            t = -t
        a = a % m
    if (m == 1):
        return t
    return 0


"""
Returns the positive and negative value of a for the equivalence described below
Algorithm described in "Prime Numbres, a computational Perspective - Richard Crandall, Carl Pomerance", 2.3.8

a : Finds a such that a^2 ≡ n(mod p)
p : A prime number part of the prime base
"""
def square_roots(a, p):
    a = a % p
    if congruent(p, 3, 8) | congruent(p, 7, 8):
        x = right_to_left_binary(a, (p+1)//4, p)
        return (x, p-x % p)
    elif congruent(p, 5, 8):
        x = right_to_left_binary(a, (p+3)//8, p)
        x = pow(a, (p+3)//8) % p
        c = (x*x) % p
        if not congruent(c, a, p):
            x = (x * pow(2, (p-1)//4)) % p
        return (x, p-x % p)
    else : # congruent(p, 1, 8)
        while True:
            d = random.randint(2, p-1)
            if legendre(d, p) == -1:
                break
        s, t = represent_as_power_of_two(p-1)
        A = right_to_left_binary(a, t, p)
        D = right_to_left_binary(d, t, p)
        m = 0
        for i in range(s):
            if congruent(pow(A*pow(D, m), pow(2, s-i-1)), -1, p):
                m += pow(2, i)
        x = (pow(a, (t+1)//2) * pow(D, m//2)) % p
        return (x, p-x % p)


"""
Returns a list of prime factors of n

prime_base : A list with primes less than base B
n : The number which we need the factors of
"""
def factor(n, prime_base):
    factors = []
    if n < 0:
        factors.append(-1)
    for p in prime_base:
        if p == -1:
            pass
        else:
            while n % p == 0:
                factors.append(p)
                n //= p
    return factors


"""
Creates a matrix from the prime factorization of the smooth values with
every row being the exponent vector reduced mod 2
"""
def create_matrix(smooth_numbers, prime_base):
    print("CREATING MATRIX")
    print("===========================================")
    K = len(smooth_numbers) - 1
    matrix = []
    
    for n in smooth_numbers:
        exp_vector = []
        factors = factor(n, prime_base)
        for prime in prime_base:
            if n % prime == 0:
                count = factors.count(prime)
                exp_vector.append(count % 2) 
            else:
                exp_vector.append(0)
        matrix.append(exp_vector)
        
    return matrix


"""
Gauss elimination in GF(2) space
https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf

Creates a matrix from the prime factorization of the smooth values with
every row being the exponent vector reduced mod 2 and 
returns a list of sets of linear dependent rows

smooth_numbers : The B-smooth values of n
prime_base : A list with primes less than base B
"""
def gauss_elimination(smooth_numbers, prime_base):
    matrix = create_matrix(smooth_numbers, prime_base)
    print("APPLYING GAUSSIAN ELIMINATION")
    print("===========================================")
    rows = len(matrix)
    columns = len(matrix[0])
    rows_marked = [False for r in range(rows)]

    for c in range(columns):
        for r in range(rows):
            if matrix[r][c] == 1:
                rows_marked[r] = True
                for k in range(columns):
                    if matrix[r][k] == 1 and k != c:
                        for i in range(rows):
                            matrix[i][k] = (matrix[i][k] + matrix[i][c]) % 2
                break

    dependent_rows = []
    for row, bool_val in enumerate(rows_marked):
        if bool_val == False:
            dependent_rows_set = {row}
            for col in range(columns):
                if matrix[row][col] == 1:
                    for r in range(rows):
                        if matrix[r][col] == 1 and r != row and rows_marked[r] == True:
                            dependent_rows_set.add(r)
            dependent_rows.append(dependent_rows_set)
    return dependent_rows
    

"""
Returns one of the two factors of n if there is a solution else 1

row_set : The rows of the prime factorization exponent vector matrix that are dependent
smooth_numbers : The B-smooth values of n
n : The number being factored
"""
def qs_factorization(row_set, smooth_numbers, smooth_x, n):
    y = 1
    x = 1
    for i in row_set:
        y *= smooth_numbers[i]
        x *= smooth_x[i]
    x = x % n
    y = int(Decimal(y).sqrt())
    y = y % n
    
    d = gcd(x - y, n)
    return d


"""
Finds the K+1 x^2 - n numbers which are B-smooth

n : The number that is being factored
prime_base : A list with primes less than base B
"""
def sieving(n, prime_base, sieve_interval):
    pair_amount = 0
    root = int(sqrt(n))
    sieve_range = sieve_interval   
    sieve_list = [x*x - n for x in range(root, root + sieve_range)]
    sieve_length = len(sieve_list)
    sieve_list_original = sieve_list[:]
    smooth_x_original = [x for x in range(root, root + sieve_range)]
    
    if prime_base[0] == 2:
        i = 0
        while sieve_list[i] % 2 != 0:
            i += 1
        for j in range(i, sieve_length, 2):
            while sieve_list[j] % 2 == 0:
                 sieve_list[j] //= 2

    for prime in prime_base[1:]:
        for residue in square_roots(n, prime):
            for i in range((residue - root) % prime, sieve_length, prime):
                while sieve_list[i] % prime == 0:
                    sieve_list[i] //= prime

    smooth_numbers = [] #The smooth-B numbers x^2 - n
    smooth_x = [] #The numbers x for which x^2 - n is smooth
    count = 0
    for i in range(sieve_length):
        if sieve_list[i] == 1:
            smooth_x.append(smooth_x_original[i])
            smooth_numbers.append(sieve_list_original[i])
            count += 1
        if count == len(prime_base) + 1:
            break
    return (smooth_x, smooth_numbers)


"""
Initializes the things needed to do the factorization

n : The number being factored
B : The B-smooth length
"""
def initilization(n, B, sieve_interval):
    prime_set = set(prime_list)
    primes = [2]
    for p in range(3, B, 2):
        if p in prime_set or (fermat_test(p, 1) and legendre(n, p) == 1 and miller_rabin(p, 3)):
            primes.append(p)
    K = len(primes)
    return (K, primes)

""""
Creates a prime base, finds B-smooth numbers, creates a matrix with the exponent vectors
of the B-smooth numbers, solves it with gauss elimination in GF(2) finding sets of dependent rows
and checks if that particular combination can produce a solution
"""
def quadratic_sieve(n, B, sieve_interval):
    try:
        print("INITIALIZING QUADRATIC SIEVE ALGORITHM")
        K, prime_base = initilization(n, B, sieve_interval)
        print("===========================================")
        print("FOUND", len(prime_base), "PRIMES")
        print("===========================================")
        print("PERFORMING SIEVING")
        print("===========================================")
        smooth_x, smooth_numbers = sieving(n, prime_base, sieve_interval)
        dependent_rows = gauss_elimination(smooth_numbers, prime_base)
        
        if len(dependent_rows): #List isnt empty therefore there are some solutions that can be tried
            for row_set in dependent_rows:
                d = qs_factorization(row_set, smooth_numbers, smooth_x, n)
                if d == 1 or d == n:
                    print("FACTORING HAS FAILED, TRYING DIFFERENT ROW COMBINATION")
                    print("===========================================")
                    pass
                else:
                    print("QUADRATIC SIEVE HAS SUCCESSFULLY FOUND A FACTORIZATION")
                    print("===========================================")
                    print(n, "CAN BE FACTORED AS:", d, "*", n//d)
                    return 1
                    break
        else:
            raise Exception
    except Exception as e:
        print ("QUADRATIC SIEVE HAS FAILED, INCREASING B")
        print("===========================================")
        print(e)
    return 0
        
"""
Main function, reads a number from the user and factors it using quadratic sieve
"""
if __name__ != "__main()__":
    n = int(input("Enter an integer bigger than 2 that is not the exponent of a prime: "))
    B = 1000
    sieve_interval = 10000
    while(not quadratic_sieve(n, B, sieve_interval)):
        B *= 2

import random
import time
from misc_functions import miller_rabin
from misc_functions import fermat_test


def naive_check(n):
    for i in range(5, 99, 2):
        if n % i == 0:
            return False
    return True


def benchmark(function):
    start = time.time()
    function()
    runtime = "{:.2f}".format((time.time() - start)/60)
    print(runtime)


"""
Generates random 2048 bit numbers and tests if the number and its sophie germain counterpart are primes
""" 
def sophie_germain():
    count = 0
    start = time.time()
    prime_found = time.time()
    while True:
        length = 2048
        p = random.getrandbits(length)
        p |= (1 << length - 1) | 1  #Set MSB and LSB to 1
        q = 2*p + 1
        z = (p - 1)//2
        count += 1
        if fermat_test(p, 1):
            if miller_rabin(p, 5):
                if fermat_test(q, 1) and miller_rabin(q, 5):
                    print(str(p) + " and \n" + str(q) + " are germain primes!")
                    break
                if fermat_test(z, 1) and miller_rabin(z, 5):
                    print(str(p) + " and \n" + str(z) + " are germain primes!")
                    break


if __name__ == "__main__":
    benchmark(sophie_germain)

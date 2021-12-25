import itertools
from hfunc import *


S_box = [[0, 2, 3, 7, 9, 12, 15, 7, 6, 15, 15, 1, 7, 3, 1, 0], [1, 5, 6, 13, 4, 1, 5, 11, 7, 8, 7, 1, 1, 3, 2, 13],
         [5, 3, 5, 12, 11, 1, 1, 5, 13, 0, 15, 7, 2, 2, 13, 0], [3, 12, 3, 11, 2, 2, 2, 4, 6, 5, 5, 0, 4, 3, 1, 0]]


def S(a):
    str_a = [str(x) for x in a]
    outer_decimal = int(str_a[0] + str_a[-1], 2)
    inner_decimal = int(''.join(str_a[1:5]), 2)
    decimal_result = S_box[outer_decimal][inner_decimal]
    # bin() cuts leading 0s so we have to add them to have a 4 bit representation
    # e.g bin(3) = 0b11 -> 0011
    binary_result = '0'*(4-len(bin(decimal_result)[2:])) + bin(decimal_result)[2:]
    return list(map(int, binary_result))


def check_eq(x, y, z):
    if (xor(S(xor(x, z)), S(z))) == y:
        return True
    return False


def diff(x,y,z):
    diff_max = -1
    for x_i in x:
        for y_i in y:
            counter = 0
            for z_i in z:
                if check_eq(x_i, y_i, z_i):
                    counter += 1
            if counter > diff_max:
                diff_max = counter
    return diff_max


if __name__ == "__main__":
    x = [list(i) for i in itertools.product([0, 1], repeat=6)]
    x.remove([0, 0, 0, 0, 0, 0])
    y = [list(i) for i in itertools.product([0, 1], repeat=4)]
    z = [list(i) for i in itertools.product([0, 1], repeat=6)]
    print(diff(x,y,z))

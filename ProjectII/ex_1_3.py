from misc_functions import right_to_left_binary
from misc_functions import factorization


if __name__ == "__main__":
    g = 13
    p = 677
    ab = 3
    n = 0
    while True:
        ab += 1
        if right_to_left_binary(g, ab, p) == 1:
            factors = factorization(ab)
            print("ab is : " + str(ab))
            first_factor = factors[0]
            second_factor = 1
            for x in factors[1:]:
                second_factor *= x
            print("a = ",first_factor, "b = ", second_factor)

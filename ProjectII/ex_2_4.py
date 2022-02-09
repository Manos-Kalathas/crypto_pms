from misc_functions import karatsuba
from misc_functions import right_to_left_binary


if __name__ == "__main__":
    m = pow(2, 107) - 1
    a = right_to_left_binary(2, 1000, m)
    b = right_to_left_binary(3, 101, m)
    c = right_to_left_binary(5, 47, m)
    result = karatsuba(karatsuba(a,b) ,c)
    print(result)
    

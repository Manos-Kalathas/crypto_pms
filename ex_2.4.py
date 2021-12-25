import random as rand
import hfunc


def left_shift(message, amount=1):
    try:
        temp = message[:amount]
        message = message[amount:]
        result = message+temp
        return result
    except IndexError:
        print("Out of index")


def find_key(crypto):
    key = []
    for i in range(16):
        key.append(c[(i+2) % LIST_SIZE] ^ c[(i+4) % LIST_SIZE] ^ c[(i+12) % LIST_SIZE] ^ c[(i+14) % LIST_SIZE])
    return key


if __name__ == "__main__":
    LIST_SIZE = 16
    m = hfunc.gen_bit_list(LIST_SIZE)
    print("message=",m)
    c = hfunc.xor(hfunc.xor(m, left_shift(m, 6)), left_shift(m, 10))
    print("crypto=",c)
    key = find_key(c)
    print("key=",key)
    print("original message=", hfunc.xor(c, key))

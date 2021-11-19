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

m = hfunc.gen_bit_list(16)
print("message=",m)
c = xor(xor(m, left_shift(m, 6)), left_shift(m, 10))
print("crypto=",c)
print("key=",xor(c,m))
#print("key=",xor(left_shift(m, 6),left_shift(m, 10)))
c = xor(xor(c, left_shift(c, 6)), left_shift(c, 10))
print("reverse=",c)

import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def cbc(aes, m):
    cipher = aes.encrypt(m)
    return cipher


def ecb(aes, m):
    cipher = aes.encrypt(m)
    return cipher


def count_bit_difference(m1, m2):
    count = 0
    for i in range(len(m1)):
        # Do xor on the bytes of each message to find how many different bits they have by counting the 1s
        xor_n = m1[i] ^ m2[i]
        count += bin(xor_n).count("1")
    return count

if __name__ == "__main__":
    key_length, IV_length, message_length = 16, 16, 32
    key = get_random_bytes(key_length)
    IV = get_random_bytes(IV_length)
    AES_ECB = AES.new(key, AES.MODE_ECB)
    AES_CBC = AES.new(key, AES.MODE_CBC, IV)
    ecb_diff, cbc_diff = 0, 0
    n_of_tests = 1000
    for i in range(n_of_tests):
        m1 = get_random_bytes(message_length)
        #Change the last bit of the last byte of each message
        m2 = m1[:message_length-1] + bytes([m1[message_length-1]^1])
        m1_ecb_encrypted = ecb(AES_ECB, m1)
        m2_ecb_encrypted = ecb(AES_ECB, m2)
        m1_cbc_encrypted = cbc(AES_CBC, m1)
        m2_cbc_encrypted = cbc(AES_CBC, m2)
        ecb_diff += count_bit_difference(m1_ecb_encrypted, m2_ecb_encrypted)
        cbc_diff += count_bit_difference(m1_cbc_encrypted, m2_cbc_encrypted)
    print("The percentage of different bits in ecb and cbc modes are: \nECB : " + "{:.2f}".format(ecb_diff/(message_length*n_of_tests*8)*100) + "% \n"
                                                                       "CBC : " + "{:.2f}".format(cbc_diff/(message_length*n_of_tests*8)*100) + "%")

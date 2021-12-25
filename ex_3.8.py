from hfunc import *


# Create the initial permutation used in RC4
def initial_permutation(seed):
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + seed[i % len(seed)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def RC4(S, m):
    length = len(m)
    i, j = 0, 0
    K = []
    for p in range(length):
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K.append(S[(S[i] + S[j]) % 256])
    return K


#Encrypt and decrypt a message based on the seed string given using RC4
def encrypt_decrypt(seed_string, message):
    seed = convert_string_to_bits(seed_string)
    bit_message = convert_string_to_bits(message)
    bit_length = len(bit_message)
    
    S = initial_permutation(seed)
    key = RC4(S, message)

    #The list with binary bits that we will xor the message with
    binary_key_list = []
    for decimal in key:
        # bin() cuts leading 0s so we have to add them to have an 8 bit representation
        # e.g bin(5) = 0b101 -> 00000101
        binary_representation = '0'*(8-len(bin(decimal)[2:])) + (bin(decimal)[2:])
        binary_key_list.extend(map(int, binary_representation))
    
    encrypted_decrypted_bit_message = xor(binary_key_list[:bit_length], bit_message)
    encrypted_decrypted_message = ''.join(convert_bits_to_string(encrypted_decrypted_bit_message))
    return encrypted_decrypted_message


if __name__ == "__main__":
    seed_string = "HOUSE"
    message = "MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE"
    enc_m = encrypt_decrypt(seed_string, message)
    dec_m = encrypt_decrypt(seed_string, enc_m)
    print("Initial message: " + message)
    print("Encrypted message: " + enc_m)
    print("Decrypted message: " + dec_m)
    
   


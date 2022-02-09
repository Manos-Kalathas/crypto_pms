from misc_functions import factorization
from misc_functions import right_to_left_binary
from misc_functions import congruent
from misc_functions import decrypt


"""
Factors the parameter N, finding p and q such that N = p*q and therefore finds euler's totient of N
We can easily then find a private key from e*d ≡ 1 (mod φ(Ν))
"""
def getPrivateKey(N, e):
    factors = factorization(N)
    p = factors[0]
    q = factors[1]
    phi = (p-1) * (q-1)
    private_key = 2
    while True:
        if congruent(e * private_key, 1, phi):
            return private_key
        private_key += 1


if __name__ == '__main__':
    encrypted_message = [3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958, 5278,
                       4674, 909, 9958, 792, 909, 4132, 3143, 9958, 3203, 5343, 792, 3143, 4443]
    N, e = (11413, 19)
    private_key = getPrivateKey(N, e)
    decrypted_string = decrypt(encrypted_message, private_key, N)
    print(decrypted_string)

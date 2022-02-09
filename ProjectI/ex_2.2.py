#pip install sympy
from sympy import *
import hfunc

def find_key():
    x = symbols('x')
    y = x**2+3*x+1
    roots = solveset(y, x)
    key = []
    for root in roots:
        key.append(int((Pow(x,5) + 3*Pow(x,3) + 7*Pow(x,2) + 3*Pow(x,4) + 5*x + 4).subs(x,root)))
    return key

if __name__ == "__main__":
    cipher = "οκηθμφδζθγοθχυκχσφθμφμχγ"
    key = find_key()
    if key[0] == key[1]:
        for letter in cipher:
            print(hfunc.shift(letter, key[0], hfunc.greek_letter_dictionary), end='')

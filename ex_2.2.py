from sympy import *
import hfunc

x = symbols('x')
y = x**2+3*x+1
roots = solveset(y, x)

for root in roots:
    key = (Pow(x,5) + 3*Pow(x,3) + 7*Pow(x,2) + 3*Pow(x,4) + 5*x + 4).subs(x,root)

# Returns a letter in the greek alphabet shifted by the number in the amount argument
# based on the greek dictionary imported
# e.g A : 1, shift by  3 -> Δ : 4
# e.g Ε : 5, shify by -2 -> Γ : 3
def shift(dictionary, letter, amount):
    greek_letter_dictionary = hfunc.greek_letter_dictionary
    letter_value = greek_letter_dictionary[letter.upper()]
    return hfunc.get_key(greek_letter_dictionary, (letter_value+amount)%24)

cipher = "οκηθμφδζθγοθχυκχσφθμφμχγ"
for letter in cipher:
    #greek_letter_dictionary = hfunc.greek_letter_dictionary
    #letter_value = greek_letter_dictionary[letter.upper()]
    print(hfunc.shift(hfunc.greek_letter_dictionary, letter, int(key)), end='')

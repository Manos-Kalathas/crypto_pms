import random as rand

def xor(message1, message2):
    try:
        assert len(message1) == len(message2)
        xor_result = []
        for index,bit in enumerate(message1):
            if bit == message2[index]:
                xor_result.append(0)
            else:
                xor_result.append(1)
        return xor_result
    except AssertionError:
        print("Messages need to be same length")


def shift(dictionary, letter, amount):
    letter_value = dictionary[letter.upper()]
    return get_key(dictionary, (letter_value-amount)%len(dictionary))


def get_key(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]

    
bit_dictionary ={
    "A" : "00000",
    "B" : "00001",
    "C" : "00010",
    "D" : "00011",
    "E" : "00100",
    "F" : "00101",
    "G" : "00110",
    "H" : "00111",
    "I" : "01000",
    "J" : "01001",
    "K" : "01010",
    "L" : "01011",
    "M" : "01100",
    "N" : "01101",
    "O" : "01110",
    "P" : "01111",
    "Q" : "10000",
    "R" : "10001",
    "S" : "10010",
    "T" : "10011",
    "U" : "10100",
    "V" : "10101",
    "W" : "10110",
    "X" : "10111",
    "Y" : "11000",
    "Z" : "11001",
    "." : "11010",
    "!" : "11011",
    "?" : "11100",
    "(" : "11101",
    ")" : "11110",
    "-" : "11111"
    }


greek_letter_dictionary ={
    "Α" : 0,
    "Β" : 1,
    "Γ" : 2,
    "Δ" : 3,
    "Ε" : 4,
    "Ζ" : 5,
    "Η" : 6,
    "Θ" : 7,
    "Ι" : 8,
    "Κ" : 9,
    "Λ" : 10,
    "Μ" : 11, 
    "Ν" : 12,
    "Ξ" : 13,
    "Ο" : 14,
    "Π" : 15,
    "Ρ" : 16,
    "Σ" : 17,
    "Τ" : 18,
    "Υ" : 19,
    "Φ" : 20,
    "Χ" : 21,
    "Ψ" : 22,
    "Ω" : 23}


english_letter_dictionary ={
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
    "I" : 8,
    "J" : 9,
    "K" : 10,
    "L" : 11, 
    "M" : 12,
    "N" : 13,
    "O" : 14,
    "P" : 15,
    "Q" : 16,
    "R" : 17,
    "S" : 18,
    "T" : 19,
    "U" : 20,
    "V" : 21,
    "W" : 22,
    "X" : 23,
    "Y" : 24,
    "Z" : 25}


def gen_bit_list(length):
    bit_message = []
    for i in range(length):
        rand.seed()
        bit_message.append(rand.randint(0,1))
    return bit_message

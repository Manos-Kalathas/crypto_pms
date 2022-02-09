import random as rand

    
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


"""
message : A string in the form of "example"
Returns a list of bits comprising of the message based on the bit dictionary
"""
def convert_string_to_bits(message):
    bit_list = []
    for char in message:
        bit_list.extend(list(bit_dictionary[char.upper()]))
    bit_list = [0 if x == '0' else 1 for x in bit_list]
    return bit_list

"""
message : A list of 0s and 1s e.g [0, 1, 0, 1]
Returns a string in the form of "example" using the bit dictionary
"""
def convert_bits_to_string(message):
    string_list = []
    message = [str(x) for x in message]
    for index in range(0, len(message), 5):
        bit_list = message[index:index+5]
        bit_string = "".join(bit_list)
        string_list.append(get_key(bit_dictionary, bit_string))
    return "".join(string_list)


"""
message1,message2 : Lists comprising of 0 and 1
Returns a list of bits with the xor of the two messages
"""
def xor(message1, message2):
    try:
        assert len(message1) == len(message2)
        xor_result = []
        for i in range(len(message1)):
            xor_result.append(message1[i] ^ message2[i])
        return xor_result
    except AssertionError:
        print("Messages need to be same length")


"""
letter : A letter found in the dictionary passed as argument
amount : How much to shift the letter
dictionary : The dictionary the letter is found in, e.g english or greek
Returns the letter after it has shifted left by the amount e.g shift(C,3) -> 'Z'
"""
def shift(letter, amount, dictionary=english_letter_dictionary):
    letter_value = dictionary[letter.upper()]
    return get_key(dictionary, (letter_value-amount)%len(dictionary))


"""
dictionary : The dictionary of the value of the key we want to get belongs to
value : The value of the key to return
Returns a char of the key that maps to the value passed e.g get_key(3) = 'D'
"""
def get_key(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]


"""
length : The length of the resulting list
Returns a list with random bits e.g [0, 1, 1, 1, ..., 1]
"""
def gen_bit_list(length):
    bit_message = []
    rand.seed()
    for i in range(length):
        bit_message.append(rand.randint(0,1))
    return bit_message

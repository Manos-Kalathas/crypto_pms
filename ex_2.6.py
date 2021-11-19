import hfunc


def convert_string_to_bits(message):
    bit_list = []
    for char in message:
        bit_list.extend(list(bit_dictionary[char.upper()]))
    bit_list = [0 if x == '0' else 1 for x in bit_list]
    return bit_list


def convert_bits_to_string(message):
    string_list = []
    message = [str(x) for x in message]
    for index in range(0, len(message), 5):
        bit_list = message[index:index+5]
        bit_string = "".join(bit_list)
        string_list.append(hfunc.get_key(bit_dictionary, bit_string))
    return string_list


if __name__ == "__main__":
    try:
        bit_dictionary = hfunc.bit_dictionary
        message = input("Enter the string to be encrypted here: ")
        bit_message = convert_string_to_bits(message)
        OTP = hfunc.gen_bit_list(len(bit_message))
        #print(OTP, bit_message)
        encrypted_bit_message = hfunc.xor(bit_message, OTP)
        encrypted_message = convert_bits_to_string(encrypted_bit_message)
        print("".join(encrypted_message))
        decrypted_bit_message = hfunc.xor(encrypted_bit_message, OTP)
        decrypted_message = convert_bits_to_string(decrypted_bit_message)
        print("".join(decrypted_message))
    except Exception as e:
        print(e)
        print("The message might have a non valid character, only use ('A-Z','.!?()-')")

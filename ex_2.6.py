import hfunc

if __name__ == "__main__":
    try:
        message = input("Enter the string to be encrypted here: ")
        bit_message = hfunc.convert_string_to_bits(message)
        OTP = hfunc.gen_bit_list(len(bit_message))
        
        encrypted_bit_message = hfunc.xor(bit_message, OTP)
        encrypted_message = hfunc.convert_bits_to_string(encrypted_bit_message)
        print(encrypted_message)
        
        decrypted_bit_message = hfunc.xor(encrypted_bit_message, OTP)
        decrypted_message = hfunc.convert_bits_to_string(decrypted_bit_message)
        print(decrypted_message)
    except Exception as e:
        print(e)
        print("The message might have a non valid character, only use ('A-Z','.!?()-')")

# An explanation of the Trithemius Cipher can be found at: https://en.wikipedia.org/wiki/Tabula_recta#Trithemius_cipher

import alphabet

def encode(message, offset=0, invert_offset=False):
    message_encoded = []
    offset_value = 1 if invert_offset else -1
    for char in message:
        index, upper_case = alphabet.index(char)
        if index != -1:
            message_encoded += alphabet.char(index + offset, upper_case)
            offset += (1 * offset_value)
        else:
            message_encoded += char
    message_encoded_final = "".join(message_encoded)
    return message_encoded_final

def decode(message, offset=0, invert_offset=False):
    return encode(message, offset, not invert_offset)

# Note: These functions can alternatively be implemented with the Vigenere Cipher (vigenere.py) with the keyword hard-coded as "abcdefghijklmnopqrstuvwxyz"
# ----- However, this removes the ability to have an optional offset
# An explanation of the Caesar Cipher can be found at: https://en.wikipedia.org/wiki/Caesar_cipher

import alphabet

def encode(message, offset):
    message_encoded = []
    for char in message:
        idx, upper_case = alphabet.index(char)
        if idx != -1:
            message_encoded.append(alphabet.char(idx - offset, upper_case))
        else:
            message_encoded.append(char)
    message_encoded_final = "".join(message_encoded)
    return message_encoded_final

def decode(message, offset):
    # To decode, offset is inverted
    return encode(message, -offset)
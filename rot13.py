# An explanation of the ROT13 cipher can be found at: https://en.wikipedia.org/wiki/ROT13

import alphabet

def encode(message):
    message_encoded = []
    for char in message:
        index, upper_case = alphabet.index(char)
        if index != -1:
            message_encoded += alphabet.char(index + 13, upper_case)
        else:
            message_encoded += char
    message_encoded_final = "".join(message_encoded)
    return message_encoded_final

def decode(message):
    return encode(message)

# Note: These functions can alternatively be implemented by calling caesar.encode() with offset hard-coded as 13
"""An explanation of the Caesar Cipher can be found at: https://en.wikipedia.org/wiki/Caesar_cipher
"""

import alphabet

def encode(message, offset):
    """Encode message with the Caesar Cipher.

    Parameters
    ----------
    message : str\n
    offset : int
    """
    message_encoded = []
    for char in message:
        index, upper_case = alphabet.index(char)
        if index != -1:
            message_encoded.append(alphabet.char(index - offset, upper_case))
        else:
            message_encoded.append(char)
    message_encoded_final = "".join(message_encoded)
    return message_encoded_final

def decode(message, offset):
    """Decode message with the Caesar Cipher.
    (Note: Offers the same functionality as caesar.encode, except offset is inverted.)

    Parameters
    ----------
    message : str \n
    offset : int
    """
    return encode(message, -offset)
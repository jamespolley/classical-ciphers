# An explanation of the Vigenère Cipher can be found at: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

import alphabet

def encode(message, keyword, invert_offset=False):
    offset_value = 1 if invert_offset else -1
    message_encoded = []
    keyword_len = len(keyword)
    keyword_idx = 0
    keyword_extended = []
    for char in message:
        if alphabet.index(char)[0] != -1:
            keyword_extended.append(keyword[keyword_idx])
            keyword_idx = (keyword_idx + 1) % keyword_len
        else:
            keyword_extended.append(char)
    for idx, char in enumerate(message):
        message_char_idx, upper_case = alphabet.index(char)
        keyword_char_idx = alphabet.index(keyword_extended[idx])[0]
        if message_char_idx != -1:
            offset = message_char_idx + (keyword_char_idx * offset_value)
            message_encoded.append(alphabet.char(offset, upper_case))
        else:
            message_encoded.append(char)
    message_encoded_final = "".join(message_encoded)
    return message_encoded_final

def decode(message, keyword, invert_offset=False):
    return encode(message, keyword, not invert_offset)
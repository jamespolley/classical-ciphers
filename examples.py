"""This file showcases examples of each cipher in this project!
"""

import caesar
import rot13
import trithemius
import vigenere

print("""
 -----------------------------------------------------
| CLASSICAL CRYPTOGRAPHY EXAMPLES (ENCODED & DECODED) |
 -----------------------------------------------------
""")

print("[ CAESAR CIPHER ]")
caesar_msg = "This method was used by Julius Caesar in his personal correspondence, hence it being named after him."
caesar_msg_enc = caesar.encode(caesar_msg, 7)
print("Cipher    >>", caesar_msg_enc)
caesar_msg_dec = caesar.decode(caesar_msg_enc, 7)
print("Plaintext >>", caesar_msg_dec)
print("About: https://en.wikipedia.org/wiki/Caesar_cipher", "\n")

print("[ROT13 CIPHER]")
rot13_msg = "This cipher is a variant of the Caesar Cipher in which each letter is replaced with the thirteenth letter after (or before) it. The process for encoding and decoding is exactly the same."
rot13_msg_enc = rot13.encode(rot13_msg)
print("Cipher    >>", rot13_msg_enc)
rot13_msg_dec = rot13.decode(rot13_msg_enc)
print("Plaintext >>", rot13_msg_dec)
print("About: https://en.wikipedia.org/wiki/ROT13", "\n")

print("[TRITHEMIUS CIPHER]")
trith_msg = "The Trithemius Cipher was invented by Johannes Trithemius and was outlined in his book Polygraphia, which is often considered the first published work on cryptology."
trith_msg_enc = trithemius.encode(trith_msg)
print("Cipher    >>", trith_msg_enc)
trith_msg_dec = trithemius.decode(trith_msg_enc)
print("Plaintext >>", trith_msg_dec)
print("About: https://en.wikipedia.org/wiki/Tabula_recta#Trithemius_cipher", "\n")

print("[ VIGENERE CIPHER ]")
vig_msg = 'Although being described as "the indecipherable cipher", a general method of cracking this cipher was eventually published three hundred years after the cipher was first described.'
vig_kw = "uncreativekeyword"
vig_msg_enc = vigenere.encode(vig_msg, vig_kw)
print("Cipher    >>", vig_msg_enc)
vig_msg_dec = vigenere.decode(vig_msg_enc, vig_kw)
print("Plaintext >>", vig_msg_dec)
print("About: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher", "\n")
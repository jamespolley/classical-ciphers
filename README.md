# **Classical Ciphers**
## Encoders and Decoders for Famous Ciphers in the History of Cryptography - Created by *jamespolley*

# **Description**
This Python package includes encoder and decoder algorithms for the following ciphers:
- Caesar
- ROT13
- Trithemius
- Vigenere

# **Usage**
**e.g. Caesar Cipher (others work in a similar way)**
```python
import caesar


message_to_encode = "This is an example of the Caesar Cipher, encoded with an offset of five."

encoded_message = caesar.encode(message_to_encode, 5)

print(encoded_message)

# Prints "Ocdn dn vi zsvhkgz ja ocz Xvznvm Xdkczm, zixjyzy rdoc vi jaanzo ja adqz."

decoded_message = caesar.decode(encoded_message, 5)

print(decoded_message)

# Prints "This is an example of the Caesar Cipher, encoded with an offset of five."
```
**For a usage example of each cipher, see examples.py**

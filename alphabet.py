"""Alphabet Index Utility

Convert alphabet character to its index, or the reverse. Enables easy manipulation of characters during process of encoding and decoding.
"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def index(char):
    """Return a tuple of:
    (1) index of character in alphabet, or -1 if not in alphabet, and
    (2) bool of whether character is upper case.

    Parameter
    ---------
    char : str (len of 1)
        Single character
    """
    upper_case = False
    index = ALPHABET.find(char)
    if index == -1:
        index = ALPHABET_UPPER.find(char)
        if index != -1:
            upper_case = True
    return index, upper_case

def char(index, upper_case=False):
    """Return character in alphabet, given its index.

    Parameters
    ----------
    index : int
        Index of character in alphabet. If index falls outside of range (0-25), it is shifted to fit within range.
    upper_case : bool, default=False
        Whether upper case. True if upper case, else False.
    """
    while index < 0 or index > 25:
        index = (index + 26) % 26
    if upper_case:
        return ALPHABET_UPPER[index]
    return ALPHABET[index]
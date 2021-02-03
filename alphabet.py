# Helper module?? -- write notes
# -------1---------2---------3---------4---------5---------6---------7---------8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def index(char):
    # Accepts a single character string -- returns a tuple consisting of:
    # --(1) the character index, or -1 if not in the alphabet
    # --(2) True if character is upper case, else False
    upper_case = False
    idx = ALPHABET.find(char)
    if idx == -1:
        idx = ALPHABET_UPPER.find(char)
        if idx != -1:
            upper_case = True
    return idx, upper_case

def char(idx, upper_case=False):
    # Accepts a character index, and whether uppercase(optional) -- returns the character
    # ----- Normalizes the index if out of range
    while idx < 0 or idx > 25:
        idx = (idx + 26) % 26
    if upper_case:
        return ALPHABET_UPPER[idx]
    return ALPHABET[idx]
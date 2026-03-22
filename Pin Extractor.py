# pin_extractor.py
# ----------------
# This is a FreeCodeCamp workshop build.
# Takes a list of poems and extracts a secret pin from each one.
# For each line in a poem, it finds the word at the position matching

# the line number and counts its letters to form a digit.
# If a line doesn't have enough words, a '0' is used instead.
# Returns a list of secret codes, one per poem.
#
# Author: Slamdad
# Date: March 2026
# Language: Python 3
# Usage: print(pin_extractor([poem1, poem2, poem3]))
# ----------------


def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = """The grass is green
here and there
hoping for rain
before it turns yellow"""

poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))




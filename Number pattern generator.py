# number_pattern.py
# -----------------
# Generates a string of integers from 1 up to n, separated by spaces.
# Example: number_pattern(4) returns "1 2 3 4"
#
# Validation:
#   - n must be an integer, otherwise returns an error message
#   - n must be greater than 0, otherwise returns an error message
#
# Author: Slamdad
# Date: March 2026
# Language: Python 3
# Usage: print(number_pattern(4))
# -----------------
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    result = ''
    for i in range(1, n+1):
         result += str(i) + ' '
    return result.strip()
print(number_pattern(4))




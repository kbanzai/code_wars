# https://www.codewars.com/kata/523f5d21c841566fde000009

import copy
def array_diff(a, b):
    return [element for element in a if not element in b]
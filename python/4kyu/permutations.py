# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

import itertools

def permutations(string):
    return list(map(lambda t: "".join(t), set(itertools.permutations(string))))
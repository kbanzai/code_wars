# https://www.codewars.com/kata/54da539698b8a2ad76000228

from functools import reduce

def isValidWalk(walk):
    if len(walk) != 10:
        return False
    directions = {
        'n': complex(1, 0),
        'e': complex(0, 1),
        's': complex(-1, 0),
        'w': complex(0, -1),
    }
    return sum(directions[w] for w in walk)  == complex(0, 0)
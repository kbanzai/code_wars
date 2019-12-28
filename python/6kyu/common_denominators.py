# https://www.codewars.com/kata/54d7660d2daf68c619000d95

import operator
from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def convertFracts(lst):
    if lst:
        denoms = [elem[1] for elem in lst]
        lcm = reduce(lambda a, b: a * b//gcd(a, b), denoms)
        return [[elem[0]*lcm//elem[1], lcm] for elem in lst]
    else:
        return lst
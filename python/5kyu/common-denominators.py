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

a = [[1, 2], [1, 3], [1, 4]]
print(convertFracts(a))
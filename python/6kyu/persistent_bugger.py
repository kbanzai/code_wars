# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

from functools import reduce
def persistence(n):
    def mul(num, count):
        if num < 10:
            return count
        else:
            return mul(reduce(lambda x,y: int(x)*int(y), str(num)), count+1)
    return mul(n, 0)

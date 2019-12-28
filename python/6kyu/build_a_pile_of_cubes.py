# https://www.codewars.com/kata/5592e3bd57b64d00f3000047

def find_nb(m):
    n = 0
    while m > 0:
        n += 1
        m -= n ** 3
    if m == 0:
        return n
    return -1
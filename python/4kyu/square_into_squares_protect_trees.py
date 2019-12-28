# https://www.codewars.com/kata/54eb33e5bc1a25440d000891


from math import sqrt

def decompose(n):
    def inner(sum, i):
        if sum == i ** 2:
            return [i]
        elif i <= 1:
            return None
        elif sum > i**2:
            arr = inner(sum - i**2, i-1)
            if arr:
                arr.append(i)
                return arr
        return inner(sum, min(int(sqrt(sum)), i-1))
    return inner(n**2, n-1)
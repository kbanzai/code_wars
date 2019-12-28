# https://www.codewars.com/kata/556deca17c58da83c00002db

from copy import copy
def tribonacci(signature, n):
    seq = []
    for i in range(n):
        if i < 3:
            seq.append(signature[i])
        else:
            seq.append(seq[i-1]+seq[i-2]+seq[i-3])
    return seq
# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

def up_array(arr):
    if not arr:
        return None
    for n in arr:
        if not n in range(0, 10):
            return None
    return [int(c) for c in str(int("".join(str(n) for n in arr)) + 1)]
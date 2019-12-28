# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints, s):
    checked = set()
    for i in ints:
        if s - i in checked:
            return [s-i, i]
        checked.add(i)
    return None
# https://www.codewars.com/kata/54da5a58ea159efa38000836

from collections import Counter

def find_it(seq):
    counts = Counter(seq)
    for num, count in counts.items():
        if count % 2:
            return num
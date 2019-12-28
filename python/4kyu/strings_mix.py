# https://www.codewars.com/kata/5629db57620258aa9d000014

import re
from collections import Counter, defaultdict
import string

def mix(s1, s2):
    strings = [re.sub(r"[^a-z]", "", s1), re.sub(r"[^a-z]", "", s2)]
    counters = [Counter(strings[0]), Counter(strings[1])]
    count_strings = defaultdict(list)
    for alphabet in string.ascii_lowercase:
        c1, c2 = counters[0][alphabet], counters[1][alphabet]
        if c1 == c2 and c1 > 1:
            count_strings[c1].append(("=", alphabet*c1))
        else:
            if c1 > c2 and c1 > 1: count_strings[c1].append(("1", alphabet*c1))
            if c2 > c1 and c2 > 1: count_strings[c2].append(("2", alphabet*c2))
    sorted_strings = []
    for c in sorted(count_strings.keys(), reverse=True):
        sorted_strings += sorted(map(lambda elem: elem[0] + ":" + elem[1], count_strings[c]))
    return "/".join(sorted_strings)
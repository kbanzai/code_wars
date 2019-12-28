# https://www.codewars.com/kata/53e57dada0cb0400ba000688

from math import factorial
from collections import Counter
from functools import lru_cache
from copy import copy

class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

def anagrams(word):
    """
        return the number of anagrams
    """
    @lru_cache()
    def get_count(count_counts):
        if 1 in count_counts and count_counts[1] == sum(count_counts.values()):
            return factorial(count_counts[1])
        count_sum = 0
        for count, count_count in count_counts.items():
            if count_count <= 0: continue
            new_count_counts = copy(count_counts)
            new_count_counts[count] -= 1
            if count > 1:
                new_count_counts[count-1] = new_count_counts.get(count-1, 0) + 1
            count_sum += count_count * get_count(new_count_counts)
        return count_sum

    char_counts = Counter(word)
    count_counts = Counter(char_counts.values())
    # use HashableDict because the return must be hashable to use lru_cache
    return get_count(HashableDict(count_counts))

def listPosition(word):
    """
        Return the anagram list position of the word
    """
    if len(word) <= 1: return 1
    chars = set(word)
    # the number of words whose first char is smaller than that of word
    head_smaller_words = sum([anagrams(word.replace(c, "", 1)) for c in chars if ord(word[0]) > ord(c)])
    return head_smaller_words + listPosition(word[1:])

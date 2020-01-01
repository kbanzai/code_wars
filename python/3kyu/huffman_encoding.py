# https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d/train/python
from collections import Counter

class Leaf():
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency

class Tree():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_encoding_rule(self):
        if type(self.left) is Leaf: left = {self.left.character: "0"}
        else: left = {character: "0"+code for character, code in self.left.get_encoding_rule().items()}
        if type(self.right) is Leaf: right = {self.right.character: "1"}
        else: right = {character: "1"+code for character, code in self.right.get_encoding_rule().items()}
        left.update(right)
        return left

    @property
    def frequency(self):
        return self.left.frequency + self.right.frequency

# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return list(Counter(s).items())

def get_encoding_rule(freqs):
    trees = [Leaf(freq[0], freq[1]) for freq in freqs]
    while len(trees) != 1:
        trees = sorted(trees, key=lambda t: t.frequency)
        trees.append(Tree(trees.pop(1), trees.pop(0)))
    return trees[0].get_encoding_rule()

def get_decoding_rule(freqs):
    encoding_rule = get_encoding_rule(freqs)
    return {encode: character for character, encode in encoding_rule.items()}

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len(freqs) <= 1: return None
    encoding_rule = get_encoding_rule(freqs)
    return "".join(encoding_rule[character] for character in s)

# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    if len(freqs) <= 1: return None
    decoding_rule = get_decoding_rule(freqs)
    decode_string = code = ""
    for b in bits:
        code += b
        if code in decoding_rule:
            decode_string += decoding_rule[code]
            code = ""
    return decode_string
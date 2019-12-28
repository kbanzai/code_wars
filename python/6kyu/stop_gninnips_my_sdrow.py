# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    words = sentence.split(" ")
    spin_words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(spin_words)

# https://www.codewars.com/kata/54a2e93b22d236498400134b

def presses(phrase):
    keyboard = ["1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9", "*", " 0", "#"]
    return sum(next(filter(lambda button: c in button, keyboard)).index(c) + 1 for c in phrase.upper())
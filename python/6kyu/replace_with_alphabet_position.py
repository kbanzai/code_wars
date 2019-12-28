# https://www.codewars.com/kata/546f922b54af40e1e90001da

import re

def alphabet_position(text):
    alphabets = re.sub(r'[^a-zA-Z]', '', text)
    return " ".join([str(ord(alphabet.lower()) - 96) for alphabet in alphabets])
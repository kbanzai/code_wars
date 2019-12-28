# https://www.codewars.com/kata/55c45be3b2079eccff00010f

import re


def order(sentence):
  return " ".join(sorted(sentence.split(), key=lambda w: int(re.search(r'[0-9]', w).group())))
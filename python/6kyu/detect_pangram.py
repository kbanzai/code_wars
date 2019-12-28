# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram(s):
    lower_s = s.lower()
    for char_num in range(ord('a'), ord('z')+1):
        if not chr(char_num) in lower_s:
            return False
    return True
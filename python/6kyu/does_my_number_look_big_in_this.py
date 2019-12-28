# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic( value ):
    string = str(value)
    length = len(string)
    return value == sum(int(digit)**length for digit in string)
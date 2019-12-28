# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

import re
from math import factorial

def combination(n, r):
    ''' return nCr '''
    return factorial(n)/factorial(r)/factorial(n-r)

def to_int(number_string):
    if number_string == "-": return -1
    if number_string == "": return 1
    return int(number_string)

def to_str(number):
    if number == -1: return "-"
    if number == 1: return ""
    return str(int(number))

def expand(expr):
    in_parenthesis = False
    power = int(expr[expr.index("^")+1:])
    if power == 0: return "1"
    in_parenthesis = expr[1:expr.index(")")]
    v = re.match(".*([a-z]).*", in_parenthesis)[1]
    v_position = in_parenthesis.index(v)
    v_number = to_int(in_parenthesis[0:v_position])
    number = to_int(in_parenthesis[v_position+1:])
    variable_numbers = [combination(power, i)*(v_number ** (power-i))*(number ** i) for i in range(power+1)]
    new_expr = ""
    for i, n in enumerate(variable_numbers):
        plus = "+" if n > 0 and i > 0 else ""
        if i == power:
            new_expr += "%s%s" % (plus, int(n))
        else:
            number = to_str(n)
            if i == power-1:
                new_expr += "%s%s%s" % (plus, number, v)
            else:
                new_expr += "%s%s%s^%s" % (plus, number, v, power-i)
    return new_expr
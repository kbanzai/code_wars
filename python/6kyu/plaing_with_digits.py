# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    m = sum(int(a)**(i+p) for i, a in enumerate(str(n)))
    return -1 if m % n else m // n
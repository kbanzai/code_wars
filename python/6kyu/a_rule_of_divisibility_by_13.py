# https://www.codewars.com/kata/564057bc348c7200bd0000ff

def thirt(n):
    m = str(n)[::-1]
    l = [1, 10, 9, 12, 3, 4]
    a = 0
    for i in range(len(m)):
        a += l[i % len(l)] * int(m[i])
    if n == a:
        return a
    return thirt(a)
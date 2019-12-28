# https://www.codewars.com/kata/59df2f8f08c6cec835000012

def meeting(s):
    names = [colon_name.split(":")[::-1] for colon_name in s.upper().split(";")]
    return "".join(map(lambda x: "(%s, %s)" % (x[0],x[1]), sorted(names, key=lambda n: n[0]+" "+n[1])))
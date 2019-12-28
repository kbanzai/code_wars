# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    l = len(names)
    if l == 0:
        return "no one likes this"
    elif l == 1:
        return "{} likes this".format(*names)
    elif l == 2:
        return "{} and {} like this".format(*names)
    elif l == 3:
        return "{}, {} and {} like this".format(*names)
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], l-2)
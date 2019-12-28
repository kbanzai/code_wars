# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

def tickets(people):
    num_25 = num_50 = 0
    for bill in people:
        if bill == 25:
            num_25 += 1
        elif bill == 50:
            if num_25 > 0:
                num_25 -= 1
                num_50 += 1
            else:
                return "NO"
        else:
            if num_50 > 0 and num_25 > 0:
                num_25 -= 1
                num_50 -= 1
            elif num_25 >= 3:
                num_25 -= 3
            else:
                return "NO"
    return "YES"
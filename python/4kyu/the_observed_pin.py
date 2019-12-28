# https://www.codewars.com/kata/5263c6999e0f40dee200059d

def get_pins(observed):
    neighbors = {
        '0': ['8'],
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['0', '5', '7', '9'],
        '9': ['6', '8'],
    }
    if len(observed) == 1:
        return neighbors[observed] + [observed]
    candidate = get_pins(observed[1:])
    return [n+c for n in neighbors[observed[0]] + [observed[0]] for c in candidate]
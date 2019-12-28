# https://www.codewars.com/kata/529bf0e9bdf7657179000008

def validSolution(board):
    def check_list(l):
        for i in l:
            if not i in range(1, 10):
                return False
        return len(set(l)) == 9

    # check rows
    for row in board:
        if not check_list(row):
            return False
    # check columns
    for column in zip(*board):
        if not check_list(column):
            return False
    # check blocks
    for i in range(3):
        for j in range(3):
            block = sum([cell[3*i: 3*(i+1)] for cell in board[3*j: 3*(j+1)]], [])
            if not check_list(block):
                return False
    return True
# https://www.codewars.com/kata/5296bc77afba8baa690002d7

def get_row(puzzle, n):
    return puzzle[n]

def get_column(puzzle, n):
    return list(list(zip(*puzzle))[n])

def get_block(puzzle, i, j):
    return [n for row in puzzle[3*i:3*(i+1)] for n in row[3*j:3*(j+1)]]

def is_solved(puzzle):
    s = set(range(1,10))
    for n in range(0, 9):
        if s != set(get_row(puzzle, n)): return False
        if s != set(get_column(puzzle, n)): return False
        if s != set(get_block(puzzle, n // 3, n % 3)): return False
    return True

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    while not is_solved(puzzle):
        for i in range(0, 9):
            for j in range(0, 9):
                if puzzle[i][j] != 0:
                    continue
                used_numbers = set(get_row(puzzle, i) + get_column(puzzle, j) + get_block(puzzle, i//3, j//3))
                candidates = [n for n in range(1, 10) if not n in used_numbers]
                if len(candidates) == 1:
                    puzzle[i][j] = candidates[0]
                    print(i, j, candidates[0])
    return puzzel
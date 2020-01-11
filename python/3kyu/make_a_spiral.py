directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_next_d(d):
    return (d + 1) % len(directions)

def in_spiral(spiral, i, j):
    return i in range(len(spiral)) and j in range(len(spiral[0]))

def can_go_straight(spiral, d, i, j):
    i_next, j_next = i+directions[d][0], j+directions[d][1]
    i_next2, j_next2 = i+(directions[d][0]*2), j+(directions[d][1]*2)
    if not in_spiral(spiral, i_next, j_next): return False
    if not in_spiral(spiral, i_next2, j_next2): return True
    return spiral[i_next2][j_next2] == 0

def can_curve(spiral, d, i, j):
    if not can_go_straight(spiral, d, i, j): return False
    next_d = get_next_d(d)
    i_front_right = i + directions[d][0] + directions[next_d][0]
    j_front_right = j + directions[d][1] + directions[next_d][1]
    return spiral[i_front_right][j_front_right] == 0

def spiralize(size):
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    spiral[0][0] = 1
    i, j, d = 0, 0, 0
    while can_curve(spiral, d, i, j):
        while can_go_straight(spiral, d, i, j):
            i, j = i+directions[d][0], j+directions[d][1]
            spiral[i][j] = 1
        d = get_next_d(d)
    return spiral

print(spiralize(8))
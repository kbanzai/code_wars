# https://www.codewars.com/kata/549ee8b47111a81214000941

def knight(p1, p2):
    def to_int_point(p):
        return (ord(p[0])-ord("a"), int(p[1])-1)
    p1 = to_int_point(p1)
    p2 = to_int_point(p2)
    points = set([p1])
    arrived = set([p1])
    distance = 0
    diffs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    while not p2 in points:
        next_points = set()
        for p in points:
            neighbors = [(diff[0]+p[0], diff[1]+p[1]) for diff in diffs]
            for p_neighbor in neighbors:
                if p_neighbor[0] in range(0, 8) and p_neighbor[1] in range(0, 8) and \
                   not p_neighbor in arrived and not p_neighbor in next_points:
                    next_points.add(p_neighbor)
            arrived.add(p)
        points = next_points
        distance += 1
    return distance
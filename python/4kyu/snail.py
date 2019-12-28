# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    if snail_map:
        top_and_right = snail_map[0] + [row[-1] for row in snail_map[1:]]
        next_map = [row[::-1][1:] for row in snail_map[1:][::-1]]
        return top_and_right + snail(next_map)
    else:
        return []
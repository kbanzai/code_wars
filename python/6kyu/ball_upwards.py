# https://www.codewars.com/kata/566be96bb3174e155300001b

def max_ball(v0):
    v0_ms = v0 * 1000 / 3600
    g = 9.81
    return round(v0_ms * 10 / g)
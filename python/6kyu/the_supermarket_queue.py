# https://www.codewars.com/kata/556deca17c58da83c00002db

def queue_time(customers, n):
    tills = [0]*n
    total = 0
    for customer in customers:
        t = min(tills)
        total += t
        tills = list(map(lambda x: x-t, tills))
        tills[tills.index(min(tills))] += customer
    return total + max(tills)
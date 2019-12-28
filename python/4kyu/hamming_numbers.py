from copy import copy
cache = [[0, 1, {1}]]

def hamming(n):
    cnt, current_hamming, computing = sorted(filter(lambda l: l[0] <= n, cache), key=lambda l: l[0])[-1]
    while cnt < n:
        cnt += 1
        current_hamming = min(computing)
        computing = copy(computing)
        computing.remove(current_hamming)
        computing.add(current_hamming * 2)
        computing.add(current_hamming * 3)
        computing.add(current_hamming * 5)        
        cache.append([cnt, current_hamming, computing])
    return current_hamming

print(hamming(10))
print(hamming(14))    
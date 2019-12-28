import heapq

def dbl_linear(n):
    pq = [1]
    heapq.heapify(pq)
    pushed = set()     
    for _ in range(0, n):
        m = heapq.heappop(pq)    
        for i in [2*m+1, 3*m+1]:    
            if not i in pushed:
                heapq.heappush(pq, i)
                pushed.add(i)
    return heapq.heappop(pq)
import heapq

def solve():
    N = int(input())
    heap = []
    for _ in range(N):
        heapq.heappush(heap, int(input()))
    
    result = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        result += (a + b)
        heapq.heappush(heap, a + b)

    print(result)

solve()

import heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, [0, start])
    d[start] = 0

    while heap:
        check, i = heapq.heappop(heap)

        if i == end:
            return d[end]

        for v, w in adj[i]:
            tmp = w + check
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, [tmp, v])

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])

start, end = map(int, input().split())

d = [100000*1000] * (N+1)
print(dijkstra(start, end))
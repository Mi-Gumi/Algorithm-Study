import heapq

def dijkstra(s):
    D = [INF]*(V+1)
    D[s] = 0
    heap = []
    heapq.heappush(heap,(0,s))

    while heap:
        d, s = heapq.heappop(heap)

        if D[s] < d:
            continue

        for nw,nx in adj_mat[s]:
            nd = d + nw
            if D[nx] > nd:
                heapq.heappush(heap,(nd,nx))
                D[nx] = nd
    return D


INF = 10**9
V,E,X = map(int,input().split())
adj_mat = [[] for _ in range(V+1)]
for i in range(E):
    s,e,d = map(int,input().split())
    adj_mat[s].append((d,e))


max_v = 0

F = dijkstra(X)
for i in range(1,V+1):
    D = dijkstra(i)
    c = D[X]  
    if max_v < F[i] + c:
        max_v = F[i] + c

print(max_v)
    
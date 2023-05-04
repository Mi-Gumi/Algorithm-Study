import heapq

N, M, X = map(int,input().split())

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

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, e, w = map(int, input().split())
    adj[a].append([e, w])


ans = [0] * (N+1)
for a in range(1,N+1):
    if a == X : continue
    d = [10000*1000] * (N+1)
    ans[a] = dijkstra(a, X)
    d = [10000*1000] * (N+1)
    ans[a] += dijkstra(X, a)
print(max(ans))
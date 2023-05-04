import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start, 0)) # distance, start, 포장
    

    while heap:
        check, now, poz = heapq.heappop(heap)

        if d[now][poz] < check:
            continue
        
        if poz + 1 <= K:
            for v, w in adj[now]:
                if d[v][poz+1] > check:
                    d[v][poz+1] = check
                    heapq.heappush(heap, (check, v, poz+1))

        for v, w in adj[now]:
            tmp = w + check
            if d[v][poz] > tmp:
                d[v][poz] = tmp
                heapq.heappush(heap, (tmp, v, poz))

adj = [tuple() for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    adj[s] += ((e, w),)
    adj[e] += ((s, w),)



d = [[1000000*10000] * (K+1) for _ in range(N+1)]


for i in range(K + 1):
    d[1][i] = 0

ans = 1000000*10000
dijkstra(1)
for i in range(K + 1):
    ans = min(ans, d[N][i])
print(ans)
import heapq
import sys
input = sys.stdin.readline

def dijkstra(x , D) :
    D[x] = 0
    Q = []
    heapq.heappush(Q, (0, x))

    while Q :
        d, town = heapq.heappop(Q)

        if D[town] < d :
            continue

        for time, v in graph[town] :
            ntime = d + time

            if D[v] > ntime :
                heapq.heappush(Q,(ntime, v))
                D[v] = ntime


n, m, x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s, e, t = map(int,input().split())
    graph[s].append((t,e))

inf = 10**9

ans = [0]*(n+1)


# 갈 때 모든 마을에서 데이크스트라
for i in range(1, n+1) :
    go = [inf]*(n+1)
    dijkstra(i, go)
    ans[i] += go[x]
# print(ans)


# 돌아올 때 x에서 데이크 스트라
go = [inf]*(n+1)
dijkstra(x, go)
for i in range(1, n+1) :
    ans[i] += go[i]
# print(ans)


# 모든 마을에서 x까지 가는 최소비용을 구하고 이건 구할 때마다 N번쩨 인덱스에 그 비용을 더해준다.
# x에서 모든 마을 가는 최소 비용 구하고 그 비용들을 더해준다.

print(max(ans))

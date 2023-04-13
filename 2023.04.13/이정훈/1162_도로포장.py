from heapq import heappop, heappush
import sys
from sys import maxsize
input = sys.stdin.readline

def dijkstra(u):
    Q = []
    D[u][k] = 0
    heappush(Q, (0, u, k))

    while Q:
        d, u , cnt = heappop(Q)

        visited[u][cnt] = 1

        if u == n :
            continue
        if D[u][cnt] < d :
            continue
        for w, v in graph[u]:
            # 포장 가능하다면 포장해서 0의 비용으로 v로 감
            if cnt > 0 and not visited[v][cnt-1]:
                if D[v][cnt-1] > d:
                    D[v][cnt-1] = d
                    heappush(Q, (d, v, cnt-1))
            # 포장하지 않고 정상적인 비용으로 v로 감
            if not visited[v][cnt] :
                nw = d + w
                if D[v][cnt] > nw:
                    D[v][cnt] = nw
                    heappush(Q, (nw, v, cnt))


n, m, k = map(int,input().split())

graph = [[] for _ in range(n+1)]
# 양방향 그래프 : 인접그래프를 전부 순회하는 경우엔 인접행렬보다 인접리스트가 유리함. 시간적 메모리적
for _ in range(m) :
    s, g, w = map(int,input().split())
    graph[s].append((w, g))
    graph[g].append((w, s))
# 방문처리
visited=[[0]*(k+1) for _ in range(n+1)]

D = [[0]*(k+1)] + [[maxsize] * (k+1) for _ in range(n)]
dijkstra(1)
print(min(D[n]))
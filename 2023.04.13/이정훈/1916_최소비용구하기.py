import heapq
from sys import maxsize
import sys
input = sys.stdin.readline

def dijkstra(u):
    Q = []
    heapq.heappush(Q, (0, u))
    D[u] = 0

    while Q:
        d, u = heapq.heappop(Q)

        if D[u] < d:
            continue

        for nw, nv in graph[u]:
            nd = d + nw

            if D[nv] > nd:
                heapq.heappush(Q, (nd, nv))
                D[nv] = nd

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
D = [maxsize] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, goal = map(int, input().split())

dijkstra(start)

print(D[goal])
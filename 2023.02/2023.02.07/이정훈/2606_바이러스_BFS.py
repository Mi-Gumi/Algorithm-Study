import sys
from collections import deque

input = sys.stdin.readline


def infect(edgearr, n):
    queue = deque([n])
    visited = [False] * (N + 1)
    visited[n] = True

    while queue:
        v = queue.popleft()
        nation.append(v)

        for i in edgearr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N = int(input().strip())
M = int(input().strip())

edge = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().strip().split())
    edge[a].append(b)
    edge[b].append(a)
nation = []
infect(edge, 1)

print(len(nation) - 1)

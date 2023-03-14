import sys
from collections import deque

input = sys.stdin.readline


def bfs(edgearr, n):
    queue = deque([n])
    visited = [False] * (N + 1)
    visited[n] = True

    while queue:
        v = queue.popleft()
        bfs_ans.append(v)

        for i in edgearr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(edgearr, n, visited):
    visited.append(n)
    dfs_ans.append(n)
    for v in edgearr[n]:
        if v not in visited:
            dfs(edgearr, v, visited)


N, M, V = map(int, input().strip().split())

edges = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().strip().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(N + 1):
    edges[i].sort()

dfs_visit = []
bfs_ans = []
dfs_ans = []

bfs(edges, V)
dfs(edges, V, dfs_visit)

print(*dfs_ans)
print(*bfs_ans)

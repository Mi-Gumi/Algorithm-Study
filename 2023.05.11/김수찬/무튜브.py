from collections import deque

def bfs(v, k):
    count = 0
    q = deque([(v, float('inf'))])
    visited = [False]*(N+1)
    visited[v] = True

    while q:
        v, min_cost = q.popleft()
        for nv, nc in graph[v]:
            if not visited[nv] and nc >= k:
                visited[nv] = True
                q.append((nv, nc))
                count += 1
    return count

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, k))
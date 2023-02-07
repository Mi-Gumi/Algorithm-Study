def infect(edgearr, n, visited):
    visited.append(n)

    for v in edgearr[n]:
        if v not in visited:
            infect(edgearr, v, visited)


N = int(input())
M = int(input())

edge = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
visited = []
infect(edge, 1, visited)

print(len(visited) - 1)

import sys
input = sys.stdin.readline

def bfs(graph, V):
    find_list = [V]
    visited = [V]
    while find_list:
        now = find_list.pop(0)
        for next in graph[now]:
            if next not in visited:
                visited.append(next)
                find_list.append(next)
    return visited

def dfs(graph, V):
    find_list = [V]
    visited = []
    while find_list:
        now = find_list.pop()
        if now not in visited:
            visited.append(now)
            find_list.extend(graph[now][::-1])
    return visited


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for vtx in graph:
    vtx.sort()

bfs_list = bfs(graph, V)
dfs_list = dfs(graph, V)

for num in dfs_list:
    print(num, end=' ')
print()

for num in bfs_list:
    print(num, end=' ')
print()
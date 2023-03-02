import sys
input = sys.stdin.readline


def dfs(graph, v, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)

    return visited

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    location = [[] for _ in range(N+1)]
    visited = []
    for _ in range(M):
        start, end = map(int,input().split())
        location[start].append(end)
        location[end].append(start)
    print(len(dfs(location, 1, visited))-1)

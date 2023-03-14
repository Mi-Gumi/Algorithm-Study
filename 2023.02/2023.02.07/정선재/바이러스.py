import sys
input = sys.stdin.readline


def dfs(graph, v, virus=[]):
    virus.append(v)
    for i in graph[v]:
        if i not in virus:
            dfs(graph, i, virus)

    return virus

T = int(input())
N = int(input())
location = [[] for _ in range(T+1)]
virus = []
for _ in range(N):
    start, end = map(int,input().split())
    location[start].append(end)
    location[end].append(start)
print(len(dfs(location, 1, virus))-1)
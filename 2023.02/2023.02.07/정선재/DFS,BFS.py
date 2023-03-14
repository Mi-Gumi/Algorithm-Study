from collections import deque
import sys
input = sys.stdin.readline


def dfs(graph, v, link=[]):
    link.append(v)
    for i in graph[v]:
        if i not in link:
            dfs(graph, i, link)

    return link

def bfs(graph, start, link=[]):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v not in link:
            link.append(v)
            queue.extend(graph[v])
    return link 

N, M, V = map(int, input().split())
location = [[] for _ in range(N+1)]
link = []
for _ in range(M):
    start, end = map(int,input().split())
    location[start].append(end)
    location[start].sort()
    location[end].append(start)
    location[end].sort()

print(*dfs(location, V))
print(*bfs(location, V))
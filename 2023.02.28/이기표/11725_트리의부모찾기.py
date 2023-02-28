import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+1)

def find_parent(v): # DFS
    for i in graph[v]:
        # 인접 정점에 해당 정점이 있거나, 방문이 안 된 경우
        if v in graph[i] and visited[i] == 0:
            visited[i] = v
            find_parent(i) # 재귀

V = int(input())
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(V-1): # 트리 생성
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
find_parent(1)
for i in range(2, V+1):
    print(visited[i])
# print(graph, visited)



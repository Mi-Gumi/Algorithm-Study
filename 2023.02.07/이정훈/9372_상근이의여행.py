from collections import deque
import sys

input = sys.stdin.readline


def travel(edgearr, n, visited):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        path.append(v)

        for i in edgearr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    edge = {}
    visited = [False] * (N + 1)
    path = []
    for i in range(M):
        start, end = map(int, input().strip().split())
        if edge.get(start):
            edge[start].append(end)
        else:
            edge[start] = [end]
        if edge.get(end):
            edge[end].append(start)
        else:
            edge[end] = [start]

    travel(edge, 1, visited)
    print(len(path) - 1)

    # class myGraph:
    # def __init__(self):
    #     self.graph = {}

    # def addInfo(self, startV, endVs):
    #     self.graph[startV] = endVs

    # def addEdge(self, startV, endV):
    #     self.graph[startV].append(endV)

    # def addVertex(self, V):
    #     self.graph[V] = []

    # def bfs(self, startV):
    #     q = [startV]
    #     visited = [startV]
    #     while q:
    #         nowV = q.pop(0)
    #     for nextV in self.graph[nowV]:
    #         if nextV not in visited:
    #             q.append(nextV)
    #         visited.append(nextV)
    #     return visited

    # def dfs(self, startV):
    #     s = [startV]
    #     visited = []
    #     while s:
    #         nowV = s.pop()
        #     if nowV not in visited:
        #         visited.append(nowV)
        #         s.extend(self.graph[nowV][::-1])
    #     return visited

    # def dfs_recursive(self, startV, visited=[]):
    #     visited.append(startV) 

    #     for nextV in self.graph[startV]:
    #         if nextV not in visited:
    #             self.dfs_recursive(nextV, visited)

    #     return visited

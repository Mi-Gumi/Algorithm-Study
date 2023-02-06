# import sys
# input = sys.stdin.readline

# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def addInfo(self, start, ends):
#         self.graph[start] = ends

#     def addEdge(self, start, end):
#         self.graph[start].append(end)

#     def addVertex(self, vertex):
#         self.graph[vertex] = []

#     def bfs(self, root):
#         find_list = [root]
#         visited = [root]
#         while find_list:
#             now = find_list.pop(0)
#             for vtx in self.graph.get(now):
#                 if vtx not in visited:
#                     visited.append(vtx)
#                     find_list.append(vtx)
#         return visited


# N = int(input())
# M = int(input())
# virus = Graph()

# for _ in range(M):
#     start, end = map(int, input().split())

#     if not virus.graph.get(start) and not virus.graph.get(end):
#         virus.addInfo(start, [end])
#         virus.addInfo(end, [start])
#     elif not virus.graph.get(start):
#         virus.addInfo(start, [end])
#         virus.addEdge(end, start)
#     elif not virus.graph.get(end):
#         virus.addEdge(start, end)
#         virus.addInfo(end, [start])
#     else:
#         virus.addEdge(start, end)
#         virus.addEdge(end, start)

# virus_list = virus.find(1)
# print(len(virus_list) - 1)

import sys
input = sys.stdin.readline

def bfs(graph, root):
    find_list = [root]
    visited = [root]
    while find_list:
        now = find_list.pop(0)
        for vtx in graph[now]:
            if vtx not in visited:
                visited.append(vtx)
                find_list.append(vtx)
    return visited


N = int(input())
M = int(input())
virus = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    virus[start].append(end)
    virus[end].append(start)

virus_list = bfs(virus, 1)
print(len(virus_list) - 1)

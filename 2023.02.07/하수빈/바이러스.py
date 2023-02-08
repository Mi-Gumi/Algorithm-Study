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

# bfs 탐색 함수
def bfs(graph, V):
    # 탐색할 노드 큐
    find_list = [V]
    # 방문한 노드 리스트
    visited = [V]
    # 탐색할 노드가 있다면
    while find_list:
        # 가장 먼저 들어온 노드를 현재 노드로 설정
        now = find_list.pop(0)
        # 현재 노드와 연결된 노드들에 대해
        for next in graph[now]:
            # 연결된 노드가 방문한 노드에 없다면
            if next not in visited:
                # 방문한 노드에 연결된 노드 추가
                visited.append(next)
                # 탐색할 노드에 연결된 노드 추가
                find_list.append(next)
    # 방문한 노드 리스트 반환
    return visited


N = int(input())
M = int(input())

# 그래프 선언
virus = [[] for _ in range(N + 1)]

# 시작 노드와 끝 노드를 받아서
for _ in range(M):
    start, end = map(int, input().split())
    # 시작 노드에 끝 노드를 연결
    virus[start].append(end)
    # 끝 노드에 시작 노드를 연결
    virus[end].append(start)

# bfs 실행
virus_list = bfs(virus, 1)

# 자신을 제외한 감염된 컴퓨터 수 출력
print(len(virus_list) - 1)

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for i in range(M): # 그래프 생성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph: # 그래프 각 노드에 연결되 노드를 오름차순으로 정렬
    g.sort()

def dfs(V):
    visited[V] = True # 방문 처리

    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]: # 방문 안했으면 dfs 탐색
            dfs(i)

def bfs(V):
    q = deque() # 데크 생성
    q.append(V) # 방문한 노드 추가
    pop_list = []
    while q: # 데크가 다 비면 탐색 종료
        x = q.popleft() # 방문 노드 pop 및 반환
        pop_list.append(x) # pop한 요소를 리스트로 만들어서 추후에 중복된 값 제거
        print(x, end=' ')
        for i in graph[x]:

            if i in pop_list: # 중복이면 밑에 과정 skip
                continue

            if not visited[i]: # 방문 안했으면
                q.append(i) # 노드 추가 및 방문 처리
                visited[i] = True


dfs(V)
visited = [False] * (N + 1)
print()
(bfs(V))








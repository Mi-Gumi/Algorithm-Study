'''
1. 인접리스트로 그래프 생성
2. 생성한 그래프를 통해 BFS 탐색
3. 시작점이 분명하지 않기때문에 역으로 목표값을 출발지점으로 하여 탐색
4. 시간을 최대값으로 갱신하며 탐색
'''
from collections import deque

def bfs(target):
    que = deque()
    que.append(target)
    time[target] = D[target] # 출발 시간을 갱신
    while que:
        node = que.popleft()
        if graph[node]: # 인접 노드가 있는 경우에만 탐색
            for v in graph[node]:
                # 현재 시간보다 큰 시간이라면 새로 갱신
                if time[v] < time[node] + D[v]:
                    time[v] = time[node] + D[v]
                    que.append(v)
# def t_sort():
#     que = deque()
#     for i in range(1, N+1):
#         if in_d[i] == 0:
#             que.append(i)
#
#     while que:
#         node = que.popleft()
#         n_time = D[node] + time[node]
#         if node == target:
#             return n_time
#         for v in graph[node]:
#             in_d[v] -= 1
#             time[v] = max(time[v], n_time)
#             if in_d[v] == 0:
#                 que.append(v)
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    D = [0] + time # 시간
    time = [0] * (N+1) # 누적 시간리스트
    # 역으로 그래프 생성
    for _ in range(K):
        v1, v2 = map(int, input().split())
        graph[v2].append(v1)
    target = int(input())
    bfs(target)
    print(max(time))
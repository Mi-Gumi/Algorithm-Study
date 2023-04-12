'''
1. 먼저 다익스트라 알고리즘을 통해 최단 경로 및 이동한 노드 저장
2. bfs 역방향 탐색으로 이전에 저장된 최단 경로와 값을 비교해 방문한 곳을 처리
3. 한번 더 다익스트라 알고리즘을 통해 방문한 경우는 제외하여 최단 경로 도출
'''
import sys, heapq
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s, e): # 최단 경로 찾기
    heap = []
    D[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        dist, node = heapq.heappop(heap)
        if D[node] < dist:
            continue
        if node == e:
            return
        for u, w in graph[node]:
            if visited[node][u]: # 최단 경로로 이미 방문한 적이 있으면 건너뛰기
                continue
            if D[u] > dist + w:
                D[u] = dist + w
                heapq.heappush(heap, (D[u], u))

def bfs(s, e): # 역방향으로 탐색하며 방문한 곳을 처리
    que = deque()
    que.append(e)

    while que:
        node = que.popleft()
        if node == s:
            continue
        for u, w in T_graph[node]:
            if not visited[u][node] and D[u] + w == D[node]:
                # 현재로 향하는 거리와 이미 기록된 거리가 같은 경우는 방문한 곳
                visited[u][node] = True
                que.append(u)


while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    start, end = map(int, input().split())
    graph = [[] for _ in range(N)]
    T_graph = [[] for _ in range(N)]
    D = [INF] * N
    visited = [[False]*N for _ in range(N)]
    for _ in range(M):
        v1, v2, w = map(int, input().split())
        graph[v1].append((v2, w))
        T_graph[v2].append((v1, w))

    # 최단 경로 기록
    dijkstra(start, end)
    # 역방향으로 기록 탐색 및 체크
    bfs(start, end)
    D = [INF] * N
    # 방문한 곳을 제외한 거의 최단 경로
    dijkstra(start, end)

    # 값이 똑같이면 거의 최단 경로 탐색 실패
    if D[end] == sys.maxsize:
        print(-1)
    else:
        print(D[end])






'''
K개의 도로를 포장하여 최소 시간 구하기 (K개 이하의 도로를 포장)
1. 0 ~ K 까지의 도로를 포장했을 때 각각의 노드에서의 최소 시간구하기
2. 최소 시간은 다익스트라 알고리즘을 활용
'''
import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
# 최소 시간을 각각의 노드에서 포장횟수만큼 구할 수 있도록 공간 설정 
D = [[INF for _ in range(K+1)] for _ in range(N+1)]
for _ in range(M):
    v1, v2, w = map(int, input().split())
    # 양방향
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

def dijkstra(s):
    heap = []
    # 가중치 노드 포장횟수
    heapq.heappush(heap, (0, s, 0))
    D[s][0] = 0

    while heap:
        dist, node, cnt = heapq.heappop(heap)
        if D[node][cnt] < dist:
            continue
        for v, we in graph[node]:
            tmp = dist + we
            # 포장을 진행하지 않는 일반적인 경우
            if D[v][cnt] > tmp:
                D[v][cnt] = tmp
                heapq.heappush(heap, (tmp, v, cnt))
            # 포장을 진행
            if cnt < K and D[v][cnt+1] > dist:
                D[v][cnt + 1] = dist
                heapq.heappush(heap, (dist, v, cnt+1))
dijkstra(1)
print(min(D[N]))


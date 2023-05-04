import heapq, sys
input = sys.stdin.readline
INF = 10**9
def dijkstra(s, e):
    heap = []
    distance[s] = 0
    visited[s] = True
    # 힙에 가중치와 시작점을 push
    heapq.heappush(heap, (0, s))
    while heap:
        # 가중치와 시작점을 pop
        dist, node = heapq.heappop(heap)
        # 도착점에 도달하면 종료 및 최소거리를 반환
        if node == e:
            return distance[e]
        for v, w in graph[node]:
            # 최소거리를 갱신
            if not visited[v] and distance[v] > dist + w:
                distance[v] = dist + w
                # 재갱신한 거리와 정점을 힙에 push
                heapq.heappush(heap, (distance[v], v))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

start, end = map(int, input().split())
print(dijkstra(start, end))
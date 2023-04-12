import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(s):
    D = [INF] * (N + 1)
    D[s] = 0
    heappush(heap, (0, s))
    while heap:
        d, now = heappop(heap)
        # 이미 현재위치의 비용이 계산되어 들어온 비용보다 낮다면 통과
        if D[now] < d:
            continue
        
        for nd, next in graph[now]:
            cost = d + nd
            if D[next] > cost:
                D[next] = cost
                heappush(heap, (cost, next))
    return D


INF = 10 ** 9
N, M, X = map(int, input().split())
heap = []
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))
# x에서 각 집으로 가는 비용 저장
ans = dijkstra(X)
for i in range(1, N + 1):
    # 각 비용에 집에서 x로 가는 비용 합산
    ans[i] += dijkstra(i)[X]
# 최댓값 출력
print(max(ans[1:]))
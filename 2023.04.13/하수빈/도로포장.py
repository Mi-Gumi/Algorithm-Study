import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra():
    while heap:
        d, s, p = heappop(heap)
        if D[p][s] < d:
            continue

        for nd, next in graph[s]:
            # 포장 안하고 지나가는 경우
            cost = nd + d
            if D[p][next] > cost:
                D[p][next] = cost
                heappush(heap, (cost, next, p))
                
            # 포장 하고 지나가는 경우
            if p < K and D[p + 1][next] > d:
                D[p + 1][next] = d
                heappush(heap, (d, next, p + 1))


INF = 10 ** 18
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# 양방향 연결
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))
    graph[e].append((d, s))

# 포장 횟수 + 1 만큼의 비용 배열 생성
D = [[INF] * (N + 1) for _ in range(K + 1)]
D[0][1] = 1
heap = []
heappush(heap, (0, 1, 0))
dijkstra()
ans = 10 ** 18
# 끝에 도착한 값들 중에서 최솟값 탐색
for i in range(K + 1):
    ans = min(ans, D[i][-1])
print(ans)
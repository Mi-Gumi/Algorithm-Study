import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline


# 경로 비활성화 함수
def check(d):
    q = deque([d])
    while q:
        now = q.popleft()
        for w, next in reverse_graph[now]:
            # 경로가 활성화 되어있고 전 경로의 최단거리에서 전 경로에서 현재위치로 오는 거리를 더했을 때 현재 거리와 같다면 사용된 경로임으로 비활성화
            if result[next] + w == result[now] and active[next][now]:
                active[next][now] = 0
                q.append(next)


def dijkstra(s):
    D = [INF] * N
    D[s] = 0
    heappush(heap, (0, s))
    while heap:
        d, now = heappop(heap)
        if D[now] < d:
            continue
        for nd, next in graph[now]:
            cost = d + nd
            if active[now][next] and D[next] > cost:
                D[next] = cost
                heappush(heap, (cost, next))
    return D


INF = 10 ** 9
while True:
    N, M = map(int, input().split())
    # 0, 0이 들어온다면 종료
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    heap = []
    graph = [[] for _ in range(N)]

    # 경로 확인을 위한 역경로 배열
    reverse_graph = [[] for _ in range(N)]

    # 경로 비활성화를 위한 배열
    active = [[1] * N for _ in range(N)]

    for _ in range(M):
        s, e, d = map(int, input().split())
        graph[s].append((d, e))
        reverse_graph[e].append((d, s))
    
    # 최단경로 탐색후 result에 저장
    result = dijkstra(S)

    # 최단경로에 사용된 경로 비활성화
    check(D)

    # 다시 다시 최단경로 탐색
    ans = dijkstra(S)[D]
    # ans가 변하지 않았다면 -1 출력 변했다면 ans 출력
    if ans == INF:
        print(-1)
    else:
        print(ans)
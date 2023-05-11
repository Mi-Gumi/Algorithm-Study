import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, limit):
    cnt = 0
    q = deque([s])
    visited = [0] * (N + 1)
    visited[s] = 1
    while q:
        now = q.popleft()
        for e, d in graph[now]:
            # 최소치 보다 d가 크고 방문한 적 없다면 추천영상에 추가
            if d >= limit and not visited[e]:
                visited[e] = 1
                q.append(e)
                cnt += 1
    print(cnt)



N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e, d = map(int, input().split())
    graph[s].append([e, d])
    graph[e].append([s, d])

for _ in range(Q):
    k, v = map(int, input().split())
    bfs(v, k)
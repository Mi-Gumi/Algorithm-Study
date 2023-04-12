import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline


# 섬을 그래프의 노드로 바꾸는 함수 섬의 영역 부분만큼 cnt로 visitied 채움
def bfs(r, c):
    visited[r][c] = cnt
    q = deque([(r, c)])
    while q:
        i, j = q.popleft()
        for di, dj in _dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and sea[ni][nj] == 1:
                visited[ni][nj] = cnt
                q.append((ni, nj))


# 섬의 위치에서 상하좌우로 직진하였을 때 만나는 다른섬이 있는지 체크 후 graph의 간선에 저장
def check(r, c):
    for dr, dc in _dir:
        tmp = 0
        nr, nc = r + dr, c + dc
        while 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc]:
                if visited[nr][nc] != visited[r][c] and tmp >= 2:
                    graph[visited[r][c]].append((tmp, visited[nr][nc]))
                break
            nr, nc = nr + dr, nc + dc
            tmp += 1


# 작성된 간선을 바탕으로 prim
def prim():
    global ans
    heappush(heap, (0, 1))
    while heap:
        d, s = heappop(heap)
        if not visited[s]:
            visited[s] = 1
            ans += d
            for v in graph[s]:
                heappush(heap, v)


N, M = map(int, input().split())
_dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
sea = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
visited = [[0] * M for _ in range(N)]
# 기록한 적 없는 섬이라면 cnt로 visited 채움
for i in range(N):
    for j in range(M):
        if not visited[i][j] and sea[i][j]:
            bfs(i, j)
            cnt += 1

graph = [[] for _ in range(cnt)]

# 간선 생성
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            check(i, j)

heap = []
ans = 0
visited = [0] * cnt
prim()

# 방문 못한 섬이 있다면 -1 아니라면 ans 출력
for n in visited[1:]:
    if not n:
        print(-1)
        break
else:
    print(ans)
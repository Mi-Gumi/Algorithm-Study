import sys
from collections import deque
input = sys.stdin.readline

# 국경선이 열리는지 확인하여 열리면 1반환
def check():
    flag = 0
    for r in range(N):
        for c in range(N):
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and L <= abs(country[r][c] - country[nr][nc]) <= R:
                    flag = 1
                    # 국경선이 열린다면 그래프에 경로 추가
                    graph[r][c].append([nr, nc])
                    graph[nr][nc].append([r, c])
    return flag


# 완성된 그래프로 bfs
def move(r, c):
    change = [[r, c]]
    visited[r][c] = 1
    q = deque([[r, c]])
    _sum = country[r][c]
    while q:
        sr, sc = q.popleft()
        for nr, nc in graph[sr][sc]:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                change.append([nr, nc])
                q.append([nr, nc])
                _sum += country[nr][nc]
    value = _sum // len(change)
    for sr, sc in change:
        country[sr][sc] = value
    

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
graph = [[[] for _ in range(N)] for _ in range(N)]
cnt = 0

# 국경선이 열린다면 반복
while check():
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 방문한 적이 없고 국경선이 연결되어 있다면 bfs
            if not visited[r][c] and graph[r][c]:
                move(r, c)
    # 국경선이 열린 횟수 추가
    cnt += 1
    graph = [[[] for _ in range(N)] for _ in range(N)]

print(cnt)
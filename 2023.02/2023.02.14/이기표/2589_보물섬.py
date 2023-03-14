import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

N, M = map(int, input().split()) # 행, 열
graph = [list(map(str, input())) for _ in range(N)]

def bfs(x, y):
    cnt = 0
    que = deque()

    que.append([x, y])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1  # 출발점은 1로 시작
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1 # 경로 이동만큼 누적 합
                cnt = max(cnt, visited[nx][ny]) # 이전 경로들과 최대값 비교
                que.append([nx, ny])
    return cnt-1 # 본인은 제외

ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j)) # 경로중에 최대값을 도출
print(ans)





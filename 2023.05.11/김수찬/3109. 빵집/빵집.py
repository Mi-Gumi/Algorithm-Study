import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1]
visited = [[0]*C for _ in range(R)]

def dfs(x, y):
    visited[x][y] = 1
    if y == C - 1:
        return 1
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == 0 and board[nx][ny] == '.':
                if dfs(nx, ny) == 1:
                    return 1
    return 0

cnt = 0
for i in range(R):
    cnt += dfs(i, 0)
print(cnt)
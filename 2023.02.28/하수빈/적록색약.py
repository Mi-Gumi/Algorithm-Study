import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


# 일반 dfs
def dfs(r, c, color):
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        # nr, nc가 범위 안에 있고 구역색이 같고 방문하지 않았다면 방문 처리 후 다시 dfs
        if 0 <= nr < N and 0 <= nc < N and region[nr][nc] == color and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, color)


# 적록색약 dfs
def dfs_weak(r, c, color):
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        # nr, nc가 범위 안에 있고 방문하지 않았다면
        if 0 <= nr < N and 0 <= nc < N and not visited_weak[nr][nc]:
            # 파란색이라면
            if color == 'B':
                # 구역색이 같다면 방문 처리 후 다시 dfs
                if region[nr][nc] == color:
                    visited_weak[nr][nc] = 1
                    dfs_weak(nr, nc, color)
            # 빨간색이거나 초록색이라면
            else:
                # 구역색이 빨간색이나 초록색이라면 방문 처리 후 다시 dfs
                if region[nr][nc] == 'R' or region[nr][nc] == 'G':
                    visited_weak[nr][nc] = 1
                    dfs_weak(nr, nc, color)


N = int(input())
region = [list(input()) for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 0
count_weak = 0
visited = [[0] * N for _ in range(N)]
visited_weak = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 일반 dfs
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, region[i][j])
            count += 1
        # 색약 dfs
        if not visited_weak[i][j]:
            visited_weak[i][j] = 1
            dfs_weak(i, j, region[i][j])
            count_weak += 1

print(f'{count} {count_weak}')

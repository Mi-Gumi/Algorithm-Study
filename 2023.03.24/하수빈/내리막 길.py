import sys
input = sys.stdin.readline

def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1
    
    # 이미 탐색했다면 return
    if visited[r][c] != -1:
        return visited[r][c]
    
    # 현재 위치에서 도착점에 도달 할 수 있는 경로 갯수는 4방향 중 낮은 위치의 경로 갯수들의 합
    tmp = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and _map[r][c] > _map[nr][nc]:
            tmp += dfs(nr, nc)

    visited[r][c] = tmp
    return visited[r][c]


N, M = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
# visited에 각 위치 마다 도착점에 도달 할 수 있는 경로 갯수 저장
visited = [[-1] * M for _ in range(N)]

print(dfs(0, 0))
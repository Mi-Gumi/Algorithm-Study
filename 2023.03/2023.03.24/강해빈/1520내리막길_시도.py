# 시간초과
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
move = [[1,0], [0,1], [-1,0], [0,-1]]
visited = [[0 for _ in range(N)] for _ in range(M)]

def dfs(x, y):
    global cnt

    if x == M-1 and y == N-1:
        cnt += 1
        return cnt

    if visited[x][y] != 0:
        return

    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if 0 <= nx < M and 0 <= ny < N:
            if matrix[x][y] > matrix[nx][ny]:
                dfs(nx, ny)
                visited[x][y] += visited[nx][ny]
    

visited[M-1][N-1] = 1
cnt = 0
dfs(0, 0)

print(cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
def dfs(i, j, pos):
    global ans
    if i == N-1 and j == N-1:
        ans += 1
        return

    # 오른쪽 0
    if (pos == 0 or pos == 2) and j+1 < N and arr[i][j+1] == 0:
        dfs(i, j+1, 0)
    # 아래 1
    if (pos == 1 or pos == 2) and i+1 < N and arr[i+1][j] == 0:
        dfs(i+1, j, 1)
    # 대각 2
    if i+1 < N and j+1 < N and arr[i+1][j+1] == 0 and arr[i+1][j] == 0 and arr[i][j+1] == 0:
        dfs(i+1, j+1, 2)

dfs(0, 1, 0)
print(ans)

import sys
sys.setrecursionlimit(10 ** 9)

def dfs(i, j):
    # 전 경로로 되돌아가며 1을 더해줌
    if i == M - 1 and j == N - 1:
        return 1

    if dp[i][j] == -1:
        # 방문 체크
        dp[i][j] = 0

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < M and 0 <= nj < N:
                # 내리막 길인 경우 DFS 재귀 탐색
                if arr[i][j] > arr[ni][nj]:
                    dp[i][j] += dfs(ni, nj)
    return dp[i][j]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

print(dfs(0, 0))


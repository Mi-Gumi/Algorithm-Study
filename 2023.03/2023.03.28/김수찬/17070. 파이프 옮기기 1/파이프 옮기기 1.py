N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]

# 0 번, 가로 // 1 번 세로 // 2번 대각성
for i in range(1,N):
    if matrix[0][i] != 1:
        dp[0][i][0] = 1 # 가로방향을 1로 설정 -> 파이프가 가로방향으로 우선적으로 깔려있음
        continue
    break


def dyanminc_programming():
    for i in range(1,N):
        for j in range(1,N):
            if (matrix[i][j] != 1) and (matrix[i][j-1] != 1) and (matrix[i-1][j] != 1):
                # 대각선으로 연결하기 위해서는 그 주변에 벽이 있으면 안됨
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2] # 대각선은 모든 방향과 연결 가능
            
            if matrix[i][j] != 1: # 가로와 세로는 그 자리에 벽이 없을 경우에 cnt 하면됨
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로방향은, 이전 파이프가 가로와 대각선일 때만 연결 가능
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 세로방향은, 이전 파이프가 가로와 대각선일 때만 세로와 대각선만 연결 가능
dyanminc_programming()
print(sum(dp[N-1][N-1]))
# dp[y][x]에서, y는 계단 수의 길이 / x는 계단 수의 맨 뒷자리에 오는 수

from sys import stdin

N = int(stdin.readline())

dp = [[0] * 10 for _ in range(N + 1)]

# 0은 제일 앞에 올 수 없으니 제외하고, 길이가 1인 계단 수의 개수 추가
for i in range(1, 10):
    dp[1][i] = 1

# 2에서 목표 길이 수까지
for i in range(2, N + 1):
    # 가능한 숫자의 범위
    for j in range(10):

        # 맨 뒷자리 수가 0이거나 9일 경우, 각 1과 8 한 가지 경우만 이어서 계단수 생성 가능
        if j == 0:
            dp[i][j] = dp[i - 1][1]

        elif j == 9:
            dp[i][j] = dp[i - 1][8]

        # 0이나 9가 아니라면 +1된 숫자 또는 -1된 숫자와 이어서 계단수 생성 가능
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)

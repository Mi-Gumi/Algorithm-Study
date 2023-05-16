import sys
input = sys.stdin.readline


N = int(input())
dp = [[0] * 10 for _ in range(101)]
# 한 자리 계단 수의 마지막 숫자 별 분류
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    for j in range(10):
        # 마지막 숫자가 0이 되려면 마지막 숫자가 1인 전 계단수에서 0 추가
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        # 마지막 숫자가 9가 되려면 마지막 숫자가 8인 전 계단수에서 9 추가
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        # 나머지 숫자는 양 쪽에서 나머지 숫자 추가
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % (10 ** 9))
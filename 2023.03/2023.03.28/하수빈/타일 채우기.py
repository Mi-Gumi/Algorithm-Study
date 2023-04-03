import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 31
dp[2] = 3
i = 4
while i <= N:
    # 규칙
    dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
    i += 2
print(dp[N])

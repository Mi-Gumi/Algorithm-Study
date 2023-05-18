def count_stairs(N):
    MOD = 1000000000
    dp = [[0] * 10 for _ in range(N + 1)]
    
    # 길이가 1인 계단 수 초기화
    for i in range(1, 10):
        dp[1][i] = 1
    
    # dp[i][j]를 구하기 위해 이전 길이의 계단 수 개수 이용
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= MOD
    
    total_count = sum(dp[N]) % MOD
    return total_count

N = int(input())
result = count_stairs(N)
print(result)
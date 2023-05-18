N = int(input())

dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]

        elif j > 0 and j < 9: 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        else:
            dp[i][j] = dp[i-1][8]
            
ans = sum(dp[N]) % 1000000000
print(ans)
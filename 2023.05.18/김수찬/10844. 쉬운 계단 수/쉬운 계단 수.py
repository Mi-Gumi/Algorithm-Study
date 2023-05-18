# import sys
N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2,N+1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][8]
    else:
      dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])

print(sum(dp[N])%1000000000)
## 이전 결과가 이후의 값에 영향을 미침
# dp = [0 for _ in range(N+1)]
# dp[1] = 9 
# dp[2] = 17 # (9-2)*2 + 2 * 2 - 1
# dp[3] = 3  # (17-2)*2 + 2 * 2

# for i in range(3,N+1):
#   dp[i] = (dp[i-1]*2 + 2*2 - (i+1)%2)%1000000000
# print(dp)
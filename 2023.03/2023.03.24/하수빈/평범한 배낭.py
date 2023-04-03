import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        # 현재 무게에 현재 물품을 넣을 수 없다면 현재 가치의 최댓값은 이전 물품을 넣었을 때 가치의 최댓값과 동일
        if j < arr[i - 1][0]:
            dp[i][j] = dp[i - 1][j]
        # 현재 무게에 현재 물품을 넣을 수 있다면
        else:
            # 현재 가치의 최댓값은 이전 물품을 넣었을 때 가치의 최댓값과 
            # 현재 무게에서 현재 물품의 무게를 뺀 무게 가치의 최댓값에서 현재 물품의 가치를 더한 값 중의 최댓값 
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1][0]] + arr[i - 1][1])

print(dp[-1][-1])
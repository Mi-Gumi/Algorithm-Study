N, K = map(int, input().split())
arr = [[0,0]]
for _ in range(N):
    W, V = map(int, input().split())
    arr.append([W, V])
arr.sort(key=lambda x : x[0])
# 버틸 수 있는 무게까지의 누적 가치합을 위한 DP
dp = [[0] * (K+1)  for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = arr[i][0]
        value = arr[i][1]
        # 무게가 더 클 경우는 이전의 가치값 저장
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 무게가 더 작을 경우 이전의 가치값과 이전의 가치값에서 무게만큼을 뺀 가치와 현재 가치의 합을 비교
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
print(dp[N][K])
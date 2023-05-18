import sys

def TSP(dp, current, visited):
    if visited == (1<<n) - 1: # 모든 도시를 방문했을 때
        return W[current][0] if W[current][0] > 0 else sys.maxsize
    
    if dp[current][visited] != -1: # 이미 계산한 경우
        return dp[current][visited]
    
    dp[current][visited] = sys.maxsize
    for i in range(1, n):
        next = 1<<i
        if visited & next == 0 and W[current][i] != 0: # 방문하지 않은 도시이며, 길이 있는 경우
            dp[current][visited] = min(dp[current][visited], TSP(dp, i, visited | next) + W[current][i])
            
    return dp[current][visited]

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(1<<n) for _ in range(n)]

print(TSP(dp, 0, 1<<0))
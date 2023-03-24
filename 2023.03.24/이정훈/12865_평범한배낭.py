N, K = map(int,input().split())

thing = [[0]*2] +[list(map(int,input().split())) for _ in range(N)]

# K : 무게
# N : 물건의 개수
memo = [[0]*(K+1) for _ in range(N+1)]

# 물건을 하나씩 추가하면서 가방의 최대무게를 늘려가면서 최대가치를 저장해놓는다.
for i in range(1,N+1) :
    for k in range(1,K+1) :
        w, v = thing[i]
        if w <= k : 
            memo[i][k] = max(memo[i-1][k], v + memo[i-1][k-w])
        else :
            memo[i][k] = memo[i-1][k]
print(memo[N][K])
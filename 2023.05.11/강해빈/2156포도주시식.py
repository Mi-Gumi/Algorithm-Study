N = int(input())
w = [int(input()) for _ in range(N)]

# print(wine) # [6, 10, 13, 9, 8, 1]

dp = [0] * N

if N == 1: # 인덱스 에러가 나는 걸 방지하기 위해 N이 1,2,3일 때 조건 설정
    dp[0] = w[0]
    ans = dp[0]
elif N == 2:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    ans = dp[1]
elif N == 3:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    dp[2] = max(w[0] + w[2], w[1] + w[2], dp[1])
    ans = dp[2]
else:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    dp[2] = max(w[0] + w[2], w[1] + w[2], dp[1])
    for i in range(3, N):
        dp[i] = max(dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i], dp[i-1])

ans = max(dp)
print(ans)

'''
dp[0] = w[0]

dp[1] = w[0] + w[1] 

dp[2] = dp[1],                      ### dp[i-1] \
        w[0] + w[2],\
        w[1] + w[2]

dp[3] = dp[2],                      ### dp[i-1] \
        w[2] + w[3],                ### dp[i-3] + w[i-1] + w[i] \
        w[0] + w[2] + w[3],         ### dp[i-3] + w[i-1] + w[i] \
        w[0] + w[1] + w[3],         ### dp[i-2] + w[i] \

dp[4] = dp[3],                      ### dp[i-1] \
        w[0] + w[1] + w[3] + w[4],  ### dp[i-3] + w[i-1] + w[i]\
        w[0] + w[2] + w[4],         ### dp[i-2] + w[i] \
        w[1] + w[2] + w[4]          ### dp[i-2] + w[i]
'''

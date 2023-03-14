N, K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

# 가치가 큰 동전부터
i = N-1
ans = 0
while K != 0 :
    # 몫 = 사용한 동전
    ans +=  K // coins[i]
    # 나머지 = 남은 돈
    K %= coins[i]
    i -= 1
        
print(ans)
        
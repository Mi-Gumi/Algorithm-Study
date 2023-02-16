N, K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

i = N-1
ans = 0
while K != 0 :
    tmp = K // coins[i]
    if  tmp  == 0:
        i -= 1
        continue
    else :
        ans += tmp
        K %= coins[i]
        i -= 1
        
print(ans)
        
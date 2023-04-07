n = int(input())
if n == 1  :
    print(0)
else :
    dp = [0]*(n+1)
    dp[2] = 3
    for i in range(4,n+1) :
        if i%2 == 1 :
            dp[i] = 0
        else :
            dp[i] = dp[i-2]*3 + sum(dp[:i-2])*2 + 2
    print(dp[n])
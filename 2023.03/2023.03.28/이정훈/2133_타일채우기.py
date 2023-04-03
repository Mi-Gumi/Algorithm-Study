N = int(input())
if N % 2:
    print(0)
else:
    N //= 2
    memo = [0] * 16
    memo[0] = 1
    memo[1] = 3
    memo[2] = 11

    for i in range(3, N+1):
        memo[i] += memo[i-1]*3
        for j in range(i-1):
            memo[i] += memo[j]*2
    print(memo[N])

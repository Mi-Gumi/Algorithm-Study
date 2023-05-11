N = int(input())

lst = [0] + [int(input()) for _ in range(N)]

def wine_tasting(n, a):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = a[1]
    dp[2] = a[1] + a[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i], dp[i - 3] + a[i - 1] + a[i])
    return dp[n]


ans = 0
if N == 1:
  ans = lst[1]
elif N == 2:
  ans = sum(lst)
elif N == 3:
  ans = max(lst[1]+lst[2], lst[2]+lst[3], lst[1]+lst[3])
else:
  ans = wine_tasting(N, lst)
print(ans)
  
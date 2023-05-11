'''
문제 : 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다. 이 중 가장 많은 양의 포도주르 마실 수 있는 경우는?
1. DP를 통해 문제를 접근
2. 개수가 1, 2, 3개인 경우는 위의 조건에 따라 최대값을 도출
3. 개수가 4이상인 경우는 3개의 점화식을 작성해 최대값을 도출
4. dp[n-1], dp[n-2]+현재 포도주, dp[n-3]+이전 포도주+현재 포도주
'''
N = int(input())
lst = [-1]
for _ in range(N):
    n = int(input())
    lst.append(n)

dp = [0] * 10001
if N == 1: dp[1] = lst[1]
elif N == 2:
    dp[1] = lst[1]
    dp[2] = lst[1] + lst[2]
elif N == 3:
    dp[1] = lst[1]
    dp[2] = lst[1] + lst[2]
    dp[3] = max(dp[2], (lst[1] + lst[3]), (lst[2] + lst[3]))
else:
    dp[1] = lst[1]
    dp[2] = lst[1] + lst[2]
    dp[3] = max(dp[2], (lst[1] + lst[3]), (lst[2] + lst[3]))
    for i in range(4, N+1):
        dp[i] = max(dp[i-1], (dp[i-2]+lst[i]), (dp[i-3]+lst[i-1]+lst[i]))
print(dp[N])
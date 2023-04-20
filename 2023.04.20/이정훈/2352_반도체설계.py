def lower_bound(target) :
    left , right = 0, len(dp)

    while left < right :
        mid = (left+right)//2
        if dp[mid] >= target :
            right = mid
        else :
            left = mid + 1
    return right


n = int(input())
arr = list(map(int,input().split()))

dp = [arr[0]]
for i in range(1,n) :
    if arr[i] > dp[-1] :
        dp.append(arr[i])
    else :
        index = lower_bound(arr[i])
        dp[index] = arr[i]

print(len(dp))
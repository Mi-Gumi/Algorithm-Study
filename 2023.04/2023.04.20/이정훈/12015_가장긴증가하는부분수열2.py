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


# 새로운 값이 dp의 마지막 값보다 크면 뒤에 추가
# 작으면 lower_bound로 들어갈 위치 (같거나 큰값) 교체
# 반복
# 반례가 발생
# 2 3 1
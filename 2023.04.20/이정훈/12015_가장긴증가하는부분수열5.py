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
# 9999 2 1 5 6
dp = [arr[0]]
index_arr = [0]
for i in range(1,n) :
    if arr[i] > dp[-1] :
        index_arr.append(len(dp))
        dp.append(arr[i])
    else :
        index = lower_bound(arr[i])
        dp[index] = arr[i]
        index_arr.append(index)

ans = []
cnt = 1
length = len(dp)
print(length)
length -= 1
for i in range(n-1, -1,-1) :
    if index_arr[i] == length :
        ans.append(arr[i])
        length -= 1

print(*ans[::-1])




# 10 
# 새로운 값이 dp의 마지막 값보다 크면 뒤에 추가
# 작으면 lower_bound로 들어갈 위치 (같거나 큰값) 교체
# 반복
# 반례가 발생
# 2 3 1
# 인덱스로 추적
# 가능한 인덱스를 다 찾고 인덱스를 증가하면서 찾는 방법
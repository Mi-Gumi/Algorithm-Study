N = int(input())
lst = list(map(int, input().split()))
cost = int(input())
start = 0
end = max(lst)

while start <= end: # 이분 탐색 진행
    mid = (start+end)//2 # 중간
    cnt = 0 # 누적합
    for i in lst:
        if i < mid: # 중간값보다 작을 경우
            cnt += i
        else:  # 중간값보다 큰 경우
            cnt += mid
    if cost >= cnt:
        start = mid + 1
    else:
        end = mid - 1
print(end)
H, W = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
# 첫번째와 마지막은 빗물 자체가 쌓일 수 없기때문에 1 ~ len-1까지
for i in range(1, len(lst)-1):
    front_max = max(lst[:i]) # 앞쪽의 max
    back_max = max(lst[i+1:]) # 뒷쪽의 max

    # 두 개 중 작은 값을 비교해 빗물 여부를 판단
    target = min(front_max, back_max)
    if lst[i] < target:
        ans += target - lst[i]

print(ans)





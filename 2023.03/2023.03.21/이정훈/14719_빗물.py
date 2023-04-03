N, M = map(int,input().split())

rain = list(map(int,input().split()))
idx = 0
water = 0
# 가장 높은 곳을 찾아 양쪽에서 high까지 순회
high = rain.index(max(rain))
for i in range(1,high) :
    if rain[i] <= rain[idx] :
        water += rain[idx] - rain[i]
    else :
        idx = i
idx = M-1
for i in range(M-2,high,-1) :
    if rain[i] <= rain[idx] :
        water += rain[idx] - rain[i]
    else :
        idx = i
        
print(water)
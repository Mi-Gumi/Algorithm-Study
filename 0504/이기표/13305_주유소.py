'''
그리디 알고리즘
1. 최소 주유소 가격을 저장하며 유지
2. 더 낮은 가격을 만나면 낮은 가격으로 비용계산
3. 더 큰 가격을 만나면 저장해 온 가격으로 비용계산
'''
N = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0
cur = 0
for i in range(len(dis)):
    if i == 0: # 큰 비용을 만나면, 저장한 비용으로 계산
        cur = cost[i]
        ans += (cur * dis[i])
        continue

    if cur < cost[i]:
        ans += (cur * dis[i])
    else: # 작은 비용을 만나면, 비용 최신화 및 계산
        cur = cost[i]
        ans += (cur * dis[i])

print(ans)


import heapq

heq = []

N, M = map(int,input().split())
lst = [ [] for _ in range(N+1)]

cnt = [ 0 for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    cnt[e] += 1
    lst[s].append(e)

for i in range(1,N+1):
    if cnt[i] == 0:
        heq.append(i)

while heq:
    now = heapq.heappop(heq)

    if lst[now]:
        for item in lst[now]:
            cnt[item] -= 1
            if cnt[item] == 0 :
                heapq.heappush(heq,item)
    print(now,end=' ')
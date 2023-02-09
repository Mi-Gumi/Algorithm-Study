import sys
input = sys.stdin.readline
N, K = map(int, input().split())

que = [i for i in range(1, N+1)]
ans = []
interval = 0

for i in range(len(que)):
    interval += (K-1) # 간격 -> 리스트에 들어가니깐 -1
    if interval >= len(que): # 간격이 큐 길이를 넘으면 나머지로 초기화
        interval = interval % len(que)
    ans.append(str(que[interval]))
    que.pop(interval)

print('<',', '.join(ans),'>', sep='')

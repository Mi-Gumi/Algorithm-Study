
N = int(input())
lst = list(map(int,input().split()))

start = 0
end = N - 1

## Idea는 만약 길이가 같을 경우, 특정 idx 위치의 item이 작을 수록 길어질 수 있기 때문에,
# item 을 교환하면서 문제를 풀어준다
# https://jainn.tistory.com/90 이분탐색의 적용 방법은 여기서 구해서 문제를 풀었다.
cnt = 0
ans = [lst[0]]
trk = [cnt]
for idx in range(1,len(lst)):
    item = lst[idx]
    if ans[-1] < item:
        ans.append(item)
        cnt = len(ans) - 1
        trk.append(cnt)
    else:
        start = 0
        end = len(ans)

        while start <= end:
            mid = (start+end)//2
            if ans[mid] < item: # 결과에 있는 mid 값이 item 보다 작다면, item 을 mid 에 넣을 수 없다,.
                start = mid + 1
            else: # ans[mid] > item: 결과에 있는 mid 값이 item 보다 크면, item 은 mid 값 보다 작은곳에 위치해야함
                end = mid - 1
        ans[start] = item # start 위치를 item과 교체
        cnt = start
        trk.append(start)
# print(lst)
# print(trk)
# print(*ans)

mx = max(trk)
m = mx
rlt = []
for idx in range(len(trk)-1,-1,-1):
  if trk[idx] == m:
    rlt.append(idx)
    m -= 1
  if m == 0 and trk[idx] == 0:
    rlt.append(idx)
    break

print(mx+1)
for idx in range(len(rlt)-1,-1,-1):
  print(lst[rlt[idx]], end=' ')